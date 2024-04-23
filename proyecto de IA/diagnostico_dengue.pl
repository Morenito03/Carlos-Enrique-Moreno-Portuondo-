% Diagnóstico de dengue basado en síntomas

diagnostico_dengue(Nombre, Fiebre, DolorCabeza, DolorArticulaciones, Nauseas) :-
    (Fiebre == 's', DolorCabeza == 's', DolorArticulaciones == 's', Nauseas == 's' ->
        write('Posible caso de dengue. Consulte a un medico, '), write(Nombre), write('.');
        write('No se cumplen suficientes sintomas para un diagnostico de dengue, '), write(Nombre), write('.')
    ).
