Feature: Lägg till en ny bok

    Scenario: Former på "Lägg till bok" sidan är tomta
        When jag tryck på "Lägg till bok" knappen i navigering menu
        Then jar ser tom titel form
        And jag ser tom författare form
        And jag ser gråtonad knappen

    Scenario: Lägga till en bok
        When jag skriver titel
        And jag skriver författare
        Then "Lägg till ny bok" knappen låser upp
        And jag tryck på knappen "Lägg till ny bok"
        Then Titelfältet är tomt
        And Författarefältet är tomt
        And "Lägg till ny bok" knappen är gråtonad

    Scenario: Visa läggad bok i Katalog
        When jag har lagt en ny bok
        And jag går till Katalog sidan
        Then jag kan se boken som jag har lagt till

    Scenario Outline: Försöka att lägga en bok utan fullständiga uppgifter
        When jag läggar eller skippar titel: <title>
        And jag läggar eller skippar författare: <author>
        Then "Lägg till ny bok" knappen är inaktiverad

        Examples:
            | title | author |
            | ""    | ""     |
            | Title | ""     |
            | ""    | Author |
