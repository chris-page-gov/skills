import { test, expect } from '@playwright/test';

test('basic assertion works', async () => {
  expect(1 + 1).toBe(2);
});
