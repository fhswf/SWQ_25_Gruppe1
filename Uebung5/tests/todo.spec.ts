import { expect, Page, test } from '@playwright/test';

test.describe('TodoMVC Tests', () => {
    test.beforeEach(async ({ page }: { page: Page }) => {
        await page.goto('https://demo.playwright.dev/todomvc/');
    });

    test("Ein neues Todo wird hinzugefügt", async ({ page }: { page: Page }) => {
        const newTodoInput = page.getByPlaceholder('What needs to be done?');
        await newTodoInput.fill('Mein erstes Todo');
        await newTodoInput.press('Enter');

        await expect(page.getByText('Mein erstes Todo')).toBeVisible();
    });

    test('leerer text', async ({ page }: { page: Page }) => {
        const newTodoInput = page.getByPlaceholder('What needs to be done?');
        await newTodoInput.click();
        await newTodoInput.click();
        await newTodoInput.fill('');
        await newTodoInput.press('Enter');
    });

    test('lange eingabe', async ({ page }: { page: Page }) => {
        const newTodoInput = page.getByPlaceholder('What needs to be done?');
        await newTodoInput.click();
        await newTodoInput.click();
        await newTodoInput.fill('Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. Donec quam felis, ultricies nec, pellentesque eu, pretium quis, sem. Nulla consequat massa quis enim. Donec pede justo, fringilla vel, aliquet nec, vulputate eget, arcu. In enim justo, rhoncus ut, imperdiet a, venenatis vitae, justo. Nullam dictum felis eu pede mollis pretium. Integer tincidunt. Cras dapibus. Vivamus elementum semper nisi. Aenean vulputate eleifend tellus. Aenean leo ligula, porttitor eu, consequat vitae, eleifend ac, enim. Aliquam lorem ante, dapibus in, viverra quis, feugiat a, tellus. Phasellus viverra nulla ut metus varius laoreet. Quisque rutrum. Aenean imperdiet. Etiam ultricies nisi vel augue. Curabitur ullamcorper ultricies nisi. Nam eget dui. Etiam rhoncus. Maecenas tempus, tellus eget condimentum rhoncus, sem quam semper libero, sit amet adipiscing sem neque sed ipsum. Nam quam nunc, blandit vel, luctus pulvinar, hendrerit id, lorem. Maecenas nec odio et ante tincidunt tempus. Donec vitae sapien ut libero venenatis faucibus. Nullam quis ante. Etiam sit amet orci eget eros faucibus tincidunt. Duis leo. Sed fringilla mauris sit amet nibh. Donec sodales sagittis magna. Sed consequat, leo eget bibendum sodales, augue velit cursus nunc,');
        await newTodoInput.press('Enter');
    });
    

    // test("mein erster test", async ({}))
    
    // TODO: Fügen Sie hier Ihre Tests ein
    // Folgen Sie den Anleitungen in der README.md
});
