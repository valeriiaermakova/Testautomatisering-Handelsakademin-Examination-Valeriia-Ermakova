Feature: Hantera märkta böcker

    Scenario Outline: Märka flera favorita böcker i Katalog
        When jag tryck på en favorit ikon nära en marklös bok <book1>
        Then bok <book1> blir märkt
        And jag tryck på favorit ikon nära andra marklös bok <book2>
        Then tidigare boken <book1> stannar som märkt
        And andra bok <book2> blir märkt
        Examples:
            | book1                                                    | book2                                   |
            | star-Hur man tappar bort sin TV-fjärr 10 gånger om dagen | star-Kaffekokaren som visste för mycket |

    Scenario: Ta bort en favoritmarkering i Katalog
        When jag tryck på favorit ikon nära en märkt bok
        Then bok blir märktlös

    Scenario: Märka en bok igen efter avmarkering
        When jag tryck på en favorit ikon nära en märkt bok
        Then boken blir märktlös
        And jag tryck på favorit ikon nära avmarkerade boken
        Then boken blir märkt

# Scenario: Kolla upp tom sida "Mina böcker"
#     When jag kollar upp "Mina böcker" sida innan jag lägger till böcker i lista
#     Then jar ser text "När du valt, kommer dina favoritböcker att visas här."

# Scenario: Favorit-märkta böcker visas i Mina böcker lista
#     When jag tryck på favorit ikon nära en marklös bok
#     And jag går till "Mina böcker"
#     Then märkta boken är i mina böcker lista
