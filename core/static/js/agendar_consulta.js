document.addEventListener('DOMContentLoaded', function() {
    const pacienteSelect = document.querySelector("select[name='paciente']");
    const alertaDiv = document.getElementById('alerta-dinamico');

    pacienteSelect.addEventListener('change', function() {
        const pacienteId = this.value;
        if (pacienteId) {
            fetch(`/paciente-info/${pacienteId}/`)
                .then(res => res.json())
                .then(data => {
                    if (data.erro) {
                        alertaDiv.style.display = 'none';
                        alertaDiv.textContent = '';
                    } else {
                        const idade = data.idade;
                        const imc = data.imc;
                        if (idade > 65 || (imc && imc > 25)) {
                            alertaDiv.style.display = 'block';
                            alertaDiv.textContent = `ATENÇÃO: Paciente ${data.nome} tem ${idade} anos e IMC ${imc} (sobrepeso).`;
                        } else {
                            alertaDiv.style.display = 'none';
                            alertaDiv.textContent = '';
                        }
                    }
                })
                .catch(() => {
                    alertaDiv.style.display = 'none';
                    alertaDiv.textContent = '';
                });
        } else {
            alertaDiv.style.display = 'none';
            alertaDiv.textContent = '';
        }
    });

    const salaSelect = document.querySelector("select[name='sala']");
    const infoSalaDiv = document.getElementById('info-sala');

    salaSelect.addEventListener('change', function() {
        const salaId = this.value;
        if (!salaId) {
            infoSalaDiv.textContent = '';
            return;
        }
        fetch(`/sala-info/${salaId}/`)
            .then(res => res.json())
            .then(data => {
                if (data.erro) {
                    infoSalaDiv.textContent = data.erro;
                } else {
                    let texto = `Sala ${data.numero_sala} - `;

                    if (data.equipamentos.length > 0) {
                        data.equipamentos.forEach(eq => {
                            texto += eq.nome;
                            if (eq.vencido) {
                                texto += ' [MANUTENÇÃO VENCIDA]';
                            }
                            texto += ', ';
                        });
                        texto = texto.slice(0, -2); // remove última vírgula e espaço
                    } else {
                        texto += "Sem equipamento";
                    }

                    if (data.ultrassom) {
                        texto += ` - Ultrassom: ${data.ultrassom.modelo} (${data.ultrassom.fabricante})`;
                    }

                    infoSalaDiv.textContent = texto;
                }
            })
            .catch(() => {
                infoSalaDiv.textContent = 'Erro ao buscar dados da sala.';
            });
    });
});
document.addEventListener('DOMContentLoaded', function () {
    const dataHoraInput = document.querySelector("input[name='data_hora']");
    const consultasDiv = document.getElementById('consultas-dia');

    dataHoraInput.addEventListener('change', function () {
        const dataHora = this.value;
        if (!dataHora) {
            consultasDiv.innerHTML = '';
            return;
        }

        const dataSomente = dataHora.split('T')[0]; // pega só a parte da data (aaaa-mm-dd)

        fetch(`/consultas-dia/?data=${encodeURIComponent(dataSomente)}`)
            .then(response => response.json())
            .then(data => {
                if (data.erro) {
                    consultasDiv.textContent = data.erro;
                } else if (data.consultas.length === 0) {
                    consultasDiv.textContent = "Não há consultas nesse dia.";
                } else {
                    let html = "<strong>Consultas agendadas para esse dia:</strong><br/><ul>";
                    data.consultas.forEach(c => {
                        html += `<li><strong>${c.nome}</strong> - ${c.hora} - Sala ${c.sala}</li>`;
                    });
                    html += "</ul>";
                    consultasDiv.innerHTML = html;
                }
            })
            .catch(() => {
                consultasDiv.textContent = "Erro ao buscar consultas.";
            });
    });
});