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

    Scenario Outline: Ta bort en favoritmarkering i Katalog
        When jag tryck på favorit ikon nära en märkt bok <bookToUnmark>
        Then bok blir märktlös <bookToUnmark>
        Examples:
            | bookToUnmark                                             |
            | star-Hur man tappar bort sin TV-fjärr 10 gånger om dagen |


    Scenario Outline: Märka en bok igen efter avmarkering
        When jag tryck på en favorit ikon nära en märkt bok <bookToReMark>
        Then boken blir märktlös <bookToReMark>
        And jag tryck på favorit ikon nära avmarkerade boken <bookToReMark>
        Then boken blir märkt <bookToReMark>
        Examples:
            | bookToReMark                                             |
            | star-Hur man tappar bort sin TV-fjärr 10 gånger om dagen |


    Scenario: Kolla upp tom sida "Mina böcker"
        When jag kollar upp "Mina böcker" sida innan jag lägger till böcker i lista
        Then jar ser text "När du valt, kommer dina favoritböcker att visas här."

    Scenario Outline: Favorit-märkta böcker visas i Mina böcker lista
        When jag tryck på favorit ikon nära en marklös bok <book>
        And jag går till "Mina böcker"
        Then märkta boken <book> är i mina böcker lista
        Examples:
            | book                                                     |
            | star-Hur man tappar bort sin TV-fjärr 10 gånger om dagen |