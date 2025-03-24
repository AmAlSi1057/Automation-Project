import { test, expect } from '@playwright/test';

test.describe('Ad-Bidding System Tests', () => {
  test.beforeAll(async ({ request }) => {
    // Setup: Clear test data or reset state
    await request.post('https://api.ad-system.com/reset');
  });

  test('Submit bid and validate response', async ({ request }) => {
    const response = await request.post('https://api.ad-system.com/bid', {
      data: { adId: '123', bidAmount: 5.0 }
    });
    expect(response.status()).toBe(200);
    const responseBody = await response.json();
    expect(responseBody).toHaveProperty('status', 'accepted');
  });

  test('Measure response time under 500ms', async ({ request }) => {
    const startTime = Date.now();
    await request.post('https://api.ad-system.com/bid', {
      data: { adId: '123', bidAmount: 5.0 }
    });
    const responseTime = Date.now() - startTime;
    expect(responseTime).toBeLessThan(500);
  });

  test('Validate error on invalid bid', async ({ request }) => {
    const response = await request.post('https://api.ad-system.com/bid', {
      data: { adId: 'invalid_id', bidAmount: -1 }
    });
    expect(response.status()).toBe(400);
  });
});
