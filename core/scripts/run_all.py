def run_all():
    from core.scripts import create_pacientes
    create_pacientes.run()

    from core.scripts import create_medicos
    create_medicos.run()

    from core.scripts import create_enfermeiras
    create_enfermeiras.run()

    from core.scripts import create_salas
    create_salas.run()

    from core.scripts import create_equipamentos
    create_equipamentos.run()

    from core.scripts import create_ultrassom
    create_ultrassom.run()

    from core.scripts import create_medicamentos
    create_medicamentos.run()

    from core.scripts import create_acolhimento
    create_acolhimento.run()

    from core.scripts import create_consulta
    create_consulta.run()

    from core.scripts import create_prescricao
    create_prescricao.run()

    from core.scripts import create_vacina
    create_vacina.run()


if __name__ == "__main__":
    run_all()