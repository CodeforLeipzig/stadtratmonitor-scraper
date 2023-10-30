from functools import reduce
from ._basic import Section
from ._header_processes import (split_by_semicolon_or_comma, extract_from_parenthesis, ignore, no_operation)


def caller(a, b):
    return (x for sub in a for x in b(sub))


class Process:
    def __init__(self, name, *funcs):
        self.name = name
        self.funcs = funcs

    def __call__(self, section: Section):
        # noinspection PyTypeChecker
        return reduce(caller, self.funcs, (section,))


class ProcessMap:
    options: tuple[Process]

    def __call__(self, section: Section):
        for opt in self.options:
            if opt.name == section.title:
                return opt(section)
        print(f'NOT FOUND: {section.title}')

    def names(self):
        return (option.name for option in self.options)


P = Process


class Headers(ProcessMap):
    options = (
        P('Betreff', ignore),
        P('Status', extract_from_parenthesis),
        P('Vorlageart', no_operation),
        P('Federführend', split_by_semicolon_or_comma),
        P('Einreicher', split_by_semicolon_or_comma),
        P('Vorlageanlass', no_operation),
        P('Beteiligt', split_by_semicolon_or_comma),
        P('Ziele', split_by_semicolon_or_comma)
    )


class Headlines(ProcessMap):
    default = P('Sachverhalt', )
    options = (
        default,
        P('Sachverhalt:', ),
        P('Antwort', ),
        P('Antwort:', ),
        P('Beschluss', ),
        P('Beschlussvorschlag', ),  # css HeaderTitle
        P('Begründung des Antrags', ),
        P('Auswirkungen auf den Stellenplan', ),
        P('Finanzielle Auswirkungen', ),
        P('Im Haushalt wirksam', ),
        P('Folgekosten Einsparungen wirksam', ),
        P('Räumlicher Bezug', ),
        P('Zusammenfassung', ),
        P('Finanz. Auswirkung', ),  # css HeaderTitle
        P('Finanzielle Auswirkungen', ),  # checkboxes
        P('Im Haushalt wirksam', ),  # checkboxes
        P('Folgekosten Einsparungen wirksam', ),  # checkboxes
        P('Steuerrechtliche Prüfung', ),  # checkboxes
        P('Auswirkungen auf den Stellenplan', ),  # checkboxes
        P('Der gemäß Ursprungsantrag gefasste Beschluss wäre', ),
        P('Hintergrund zum Beschlussvorschlag:', ),
        P('Welche strategischen Ziele werden mit der Maßnahme unterstützt?', ),
        P('2030 – Leipzig wächst nachhaltig!', ),
        P('Ziele und Handlungsschwerpunkte', ),
        P('Klimawirkung durch den Beschluss der Vorlage', ),
        P('Stufe 1: Grobe Einordnung zur Klimawirkung (Klimaschutzes und zur –wandelanpassung)', ),
        P('Stufe 2: Die Vorlage berücksichtigt die zentralen energie- und klimapolitischen Beschlüsse', ),
        P('Stufe 3: Detaillierte Darstellung zur abschätzbaren Klimawirkung nur bei erheblicher Relevanz', ),
        P('Beschreibung des Abwägungsprozesses:', ),
        P('I. Eilbedürftigkeitsbegründung', ),
        P('II. Begründung Nichtöffentlichkeit', ),
        P('III.  Strategische Ziele', ),
        P('IV. Sachverhalt', ),
        P('Begründung Nichtöffentlichkeit', ),
        P('Eilbedürftigkeitsbegründung', ),
        P('Strategische Ziele'),
        P('I.'),
        P('II.'),
        P('III.'),
        P('IV.'),
        P('1. Begründung Kreuz auf dem Deckblatt', ),
        P('2. Realisierungs- / Zeithorizont (entfällt bei Ablehnung des Antrags)', ),
        P('Begründung Kreuz auf dem Deckblatt', ),
        P('Realisierungs- / Zeithorizont (entfällt bei Ablehnung des Antrags)', ),
        P('Realisierungs- / Zeithorizont', ),
        P('1.', ),
        P('2.', ),
        P('Begründung', ),
        P('Begründung:', ),
        P('Zusammenfassung', ),
        P('Rechtliche Konsequenzen', )
    )


HEADERS = Headers()
HEADLINES = Headlines()
