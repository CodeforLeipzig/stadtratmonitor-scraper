from functools import reduce
from ._header_processes import (split_by_semicolon_or_comma, clean_outer_spaces, extract_from_parenthesis, ignore,
                                no_operation)


def caller(a, b):
    yield from (y for x in a for y in b(x))


class Process:
    def __init__(self, name, *funcs):
        self.name = name
        self.funcs = funcs

    def __call__(self, section):
        # noinspection PyTypeChecker
        yield from reduce(caller, self.funcs, (section,))


class ProcessMap:
    options: tuple[Process]

    def __call__(self, section):
        for opt in self.options:
            if opt.name == section.title:
                return opt(section)


P = Process


class Headers(ProcessMap):
    options = (
        P('Betreff', ignore),
        P('Status', extract_from_parenthesis),
        P('Vorlageart', no_operation),
        P('Federführend', split_by_semicolon_or_comma),
        P('Einreicher', split_by_semicolon_or_comma),
        P('Vorlageanlass', no_operation),
        P('Beteiligt', split_by_semicolon_or_comma)
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
        P('1. Begründung Kreuz auf dem Deckblatt', ),
        P('Begründung', ),
        P('Begründung:', ),
        P('2. Realisierungs- / Zeithorizont (entfällt bei Ablehnung des Antrags)', ),
        P('Zusammenfassung', ),
        P('Rechtliche Konsequenzen', )
    )
