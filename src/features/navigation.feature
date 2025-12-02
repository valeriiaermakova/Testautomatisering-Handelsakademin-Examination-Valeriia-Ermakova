Feature: Webbplats navigering

    Scenario: Landning på huvudsida
        When jag öppna Läslista webbsida
        Then jag är på Katalog vy

    Scenario: Navigering till "Lägg till bok" vy
        When jag trick på "Lägg till bok"
        Then jag är på "Lägg till bok" vy

    Scenario: Navigering till "Mina böcker" vy
        When jag trick på "Mina böcker"
        Then jag är på "Mina böcker" vy

    Scenario: Navigering tillbaka till "Katalog" vy
        When jag är på "Mina böcker" vy
        And jag trick på "Katalog"
        Then jag är på "Katalog" vy