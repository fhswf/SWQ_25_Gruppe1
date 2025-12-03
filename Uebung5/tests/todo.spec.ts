import { expect, Page, test } from '@playwright/test';

const TODO_URL = 'https://demo.playwright.dev/todomvc/';

// Helper: fügt ein Todo via Eingabe und Enter hinzu
async function addTodo(page: Page, text: string) {
    const input = page.getByPlaceholder('What needs to be done?');
    await input.fill(text);
    await input.press('Enter');
}


test.describe('TodoMVC - Grundlegend', () => {
    test.beforeEach(async ({ page }) => {
        await page.goto(TODO_URL);
    });

    test('Ein Todo hinzufügen', async ({ page }) => {
        // Erwartet: Nach Eingabe erscheint der Eintrag in der Liste und Zähler ist korrekt
        await addTodo(page, 'Mein erstes Todo');
        await expect(page.getByText('Mein erstes Todo')).toBeVisible();
        await expect(page.locator('.todo-count')).toHaveText('1 item left');
    });

    test('Mehrere Todos hinzufügen', async ({ page }) => {
        await addTodo(page, 'Todo 1');
        await addTodo(page, 'Todo 2');
        await addTodo(page, 'Todo 3');

        const items = page.locator('.todo-list li');
        await expect(items).toHaveCount(3);
        await expect(page.locator('.todo-count')).toHaveText('3 items left');
    });

    test('Checkboxen setzen und items left prüfen', async ({ page }) => {
        await addTodo(page, 'A');
        await addTodo(page, 'B');

        const firstToggle = page.locator('.todo-list li').first().locator('input.toggle');
        await firstToggle.check();
        await expect(firstToggle).toBeChecked();

        // Nach einem gesetzten Haken sollte der Zähler 1 item left anzeigen
        await expect(page.locator('.todo-count')).toHaveText('1 item left');
    });
});


test.describe('TodoMVC - Löschen & Toggle-All', () => {
    test.beforeEach(async ({ page }) => {
        await page.goto(TODO_URL);
    });

    test('Todo via X (Hover) löschen', async ({ page }) => {
        await addTodo(page, 'zu löschen');
        const item = page.locator('.todo-list li').first();
        await item.hover();
        // Löschen-Button ist ein button.destroy
        await item.locator('button.destroy').click();
        await expect(page.getByText('zu löschen')).toHaveCount(0);
    });

    test('Toggle-All setzt alle Todos auf erledigt / nicht erledigt', async ({ page }) => {
        await addTodo(page, 'T1');
        await addTodo(page, 'T2');

        const toggleAll = page.locator('.toggle-all');
        // Toggle all: setzt alle auf erledigt
        await toggleAll.click();
        await expect(page.locator('.todo-list li .toggle')).toHaveCount(2);
        await expect(page.locator('.todo-list li .completed')).toHaveCount(2);

        // Nochmal klicken klappt: setzt alle wieder zurück (nicht erledigt)
        await toggleAll.click();
        await expect(page.locator('.todo-list li.completed')).toHaveCount(0);
    });

    test('Clear completed entfernt erledigte Einträge', async ({ page }) => {
        await addTodo(page, 'c1');
        await addTodo(page, 'c2');
        // markiere beide
        await page.locator('.todo-list li').first().locator('input.toggle').check();
        await page.locator('.todo-list li').nth(1).locator('input.toggle').check();

        // Clear completed erscheint und entfernt erledigte
        await page.getByRole('button', { name: 'Clear completed' }).click();
        await expect(page.locator('.todo-list li')).toHaveCount(0);
    });
});


test.describe('TodoMVC - Filter', () => {
    test.beforeEach(async ({ page }) => {
        await page.goto(TODO_URL);
        await addTodo(page, 'a1');
        await addTodo(page, 'a2');
        await addTodo(page, 'a3');
        // markiere das zweite als erledigt
        await page.locator('.todo-list li').nth(1).locator('input.toggle').check();
    });

    test('Active filter zeigt nur offene Todos', async ({ page }) => {
        await page.getByRole('link', { name: 'Active' }).click();
        await expect(page.locator('.todo-list li')).toHaveCount(2);
        await expect(page.locator('.todo-count')).toHaveText('2 items left');
    });

    test('Completed filter zeigt nur erledigte Todos', async ({ page }) => {
        await page.getByRole('link', { name: 'Completed' }).click();
        await expect(page.locator('.todo-list li')).toHaveCount(1);
    });

    test('All filter zeigt alle Todos', async ({ page }) => {
        await page.getByRole('link', { name: 'All' }).click();
        await expect(page.locator('.todo-list li')).toHaveCount(3);
    });
});


test.describe('TodoMVC - Edge Cases', () => {
    test.beforeEach(async ({ page }) => {
        await page.goto(TODO_URL);
    });

    test('Leere Eingabe (Enter ohne Text) erzeugt kein Todo', async ({ page }) => {
        const input = page.getByPlaceholder('What needs to be done?');
        await input.fill('');
        await input.press('Enter');
        await expect(page.locator('.todo-list li')).toHaveCount(0);
    });

    test('Sehr langer Text wird akzeptiert', async ({ page }) => {
        const longText = 'A'.repeat(1000);
        await addTodo(page, longText);
        await expect(page.getByText(longText)).toBeVisible();
    });

    test('Clear completed nicht sichtbar ohne Todos', async ({ page }) => {
        // ohne Todos gibt es keinen Button 'Clear completed'
        await expect(page.getByRole('button', { name: 'Clear completed' })).toBeHidden();
    });
});

// Struktur/Refactor: Helper-Funktion `addTodo` und Konstanten verwendet
