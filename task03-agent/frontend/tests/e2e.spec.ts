import { test, expect } from '@playwright/test';

test.describe('Autonomous Research Agent Dashboard', () => {
  test('should load the configuration page, trigger a run, display streaming updates, and export reports', async ({ page }) => {
    // 1. Mock the initiate run POST request
    await page.route('**/api/v1/agent/run', async (route) => {
      await route.fulfill({
        status: 200,
        contentType: 'application/json',
        body: JSON.stringify({
          success: true,
          run_id: 'test-run-123',
          message: 'Research run started successfully.',
        }),
      });
    });

    // 2. Mock the SSE event stream GET request
    await page.route('**/api/v1/agent/stream/test-run-123', async (route) => {
      const sseBody = [
        'data: {"type": "reasoning", "run_id": "test-run-123", "data": {"text": "Searching competitors..."}}\n\n',
        'data: {"type": "cost", "run_id": "test-run-123", "data": {"input_tokens": 120, "output_tokens": 85, "total_tokens": 205, "total_usd": 0.00025, "cumulative_usd": 0.00025}}\n\n',
        'data: {"type": "report", "run_id": "test-run-123", "data": {"markdown": "# Market Report\\nTop competitors: Garmin, Apple.", "charts": [{"name": "market_share.png", "base64": "iVBORw0KGgoAAAANSUhEUgAAAAEAAAABCAAAAAA6fptVAAAACklEQVR42mNkYAAAAAYAAjCB0C8AAAAASUVORK5CYII="}]}}\n\n',
        'data: {"type": "done", "run_id": "test-run-123", "data": {"run_id": "test-run-123"}}\n\n'
      ].join('');

      await route.fulfill({
        status: 200,
        headers: {
          'Content-Type': 'text/event-stream',
          'Cache-Control': 'no-cache',
          'Connection': 'keep-alive',
        },
        body: sseBody,
      });
    });

    // 3. Mock the export report endpoints
    await page.route('**/api/v1/agent/report/test-run-123/pdf', async (route) => {
      await route.fulfill({
        status: 200,
        contentType: 'application/pdf',
        headers: {
          'Content-Disposition': 'attachment; filename="report-test-run.pdf"',
        },
        body: Buffer.from('%PDF-1.4...'), // Mock PDF header
      });
    });

    // 4. Visit the dashboard home page
    await page.goto('/');

    // 5. Assert the initial layout is present
    await expect(page.locator('h1')).toContainText('Autonomous Research Agent');
    await expect(page.locator('#status-badge')).toContainText('idle');

    // 6. Fill in the research topic and adjust budget
    const topicInput = page.locator('#topic-input');
    await expect(topicInput).toHaveValue('wearable technology competitive landscape top 5 competitors');
    await topicInput.fill('Smart ring competitive landscape');

    // Adjust budget slider
    const budgetSlider = page.locator('#budget-slider');
    await budgetSlider.evaluate((el: HTMLInputElement) => {
      el.value = '2.50';
      el.dispatchEvent(new Event('input', { bubbles: true }));
      el.dispatchEvent(new Event('change', { bubbles: true }));
    });

    // 7. Click Start Research Run
    const startBtn = page.locator('#start-btn');
    await expect(startBtn).toBeEnabled();
    await startBtn.click();

    // 8. Assert streaming execution and status completed
    await expect(page.locator('#status-badge')).toContainText('completed');

    // 9. Verify live terminal logs were received
    const logsTerminal = page.locator('#terminal-logs');
    await expect(logsTerminal).toContainText('Searching competitors...');

    // 10. Verify tokens and budget usage tracking UI updates
    const costStats = page.locator('#cost-stats');
    await expect(costStats).toContainText('120'); // input tokens
    await expect(costStats).toContainText('85');  // output tokens
    await expect(costStats).toContainText('205'); // combined tokens

    // 11. Verify markdown report rendered successfully
    const mdReport = page.locator('#report-markdown');
    await expect(mdReport).toContainText('Market Report');
    await expect(mdReport).toContainText('Top competitors: Garmin, Apple.');

    // 12. Verify matplotlib chart was rendered
    const chartsContainer = page.locator('#report-charts');
    await expect(chartsContainer.locator('img')).toBeVisible();

    // 13. Test report downloading (exporting)
    const exportMdBtn = page.locator('#export-md-btn');
    await expect(exportMdBtn).toBeEnabled();
    const [mdDownload] = await Promise.all([
      page.waitForEvent('download'),
      exportMdBtn.click(),
    ]);
    expect(mdDownload.suggestedFilename()).toContain('.md');

    const exportPdfBtn = page.locator('#export-pdf-btn');
    await expect(exportPdfBtn).toBeEnabled();
    const [pdfDownload] = await Promise.all([
      page.waitForEvent('download'),
      exportPdfBtn.click(),
    ]);
    expect(pdfDownload.suggestedFilename()).toContain('.pdf');
  });
});
