Feature: Webbsida vy

    Scenario: Check Main header
        When jag är på Läslistan webbsida
        Then jag ser text "Läslistan"
        And jag ser en kontextuell bild

    Scenario: Check webbsida titel vy
        When jag är på Läslista webbsida
        Then jag ser text Läslistan son sidas titel