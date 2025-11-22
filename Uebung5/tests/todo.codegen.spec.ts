import { test, expect } from '@playwright/test';

test('test', async ({ page }) => {
  await page.goto('https://demo.playwright.dev/todomvc/#/');
  await page.locator('html').click();
  await page.getByRole('textbox', { name: 'What needs to be done?' }).click();
  await page.getByRole('textbox', { name: 'What needs to be done?' }).fill('test \' my \'cases \'or 1 = 1 ;');
  await page.getByRole('textbox', { name: 'What needs to be done?' }).press('Enter');
  await page.getByRole('checkbox', { name: 'Toggle Todo' }).check();
  await page.getByRole('checkbox', { name: 'Toggle Todo' }).uncheck();
  await page.getByRole('textbox', { name: 'What needs to be done?' }).click();
  await page.getByRole('textbox', { name: 'What needs to be done?' }).fill('tbjs');
  await page.getByRole('textbox', { name: 'What needs to be done?' }).press('Enter');
  await page.getByRole('textbox', { name: 'What needs to be done?' }).press('Enter');
  await page.getByRole('textbox', { name: 'What needs to be done?' }).fill('tnks');
  await page.getByRole('textbox', { name: 'What needs to be done?' }).press('Enter');
  await page.getByRole('listitem').filter({ hasText: 'tbjs' }).getByLabel('Toggle Todo').check();
  await page.getByRole('listitem').filter({ hasText: 'test \' my \'cases \'or 1 = 1 ;' }).getByLabel('Toggle Todo').check();
  await page.getByRole('link', { name: 'Completed' }).click();
  await page.getByRole('link', { name: 'Active' }).click();
  await page.getByRole('link', { name: 'All' }).click();
  await page.getByRole('button', { name: 'Clear completed' }).click();
  await page.getByTestId('todo-title').dblclick();
  await page.getByRole('textbox', { name: 'Edit' }).click({
    button: 'right'
  });
  await page.getByRole('textbox', { name: 'Edit' }).hover();
  await page.locator('html').click();
  await page.getByRole('textbox', { name: 'What needs to be done?' }).press('ControlOrMeta+ControlOrMeta+j');
  await page.goto('https://demo.playwright.dev/todomvc/#/');
  await page.locator('html').click();
  await page.locator('html').click();
  await page.locator('html').click();
});