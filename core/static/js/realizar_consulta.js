document.addEventListener('DOMContentLoaded', function() {
    const campoDataHora = document.querySelector('input[name="data_hora"]');
    const ulConsultas = document.getElementById('consultas-dia-lista');

    function buscarConsultasPorDia(dataCompleta) {
        const data = dataCompleta.split('T')[0];  // Extrai yyyy-mm-dd
        fetch(`/consultas-dia/?data=${data}`)
            .then(response => response.json())
            .then(data => {
                ulConsultas.innerHTML = '';
                if (data.consultas && data.consultas.length > 0) {
                    data.consultas.forEach(c => {
                        const li = document.createElement('li');
                        li.textContent = `${c.nome} - ${c.hora} - Sala ${c.sala}`;
                        ulConsultas.appendChild(li);
                    });
                } else {
                    ulConsultas.innerHTML = '<li>Não há consultas nesse dia.</li>';
                }
            })
            .catch(err => {
                ulConsultas.innerHTML = '<li>Erro ao buscar as consultas.</li>';
                console.error(err);
            });
    }

    if (campoDataHora) {
        campoDataHora.addEventListener('change', function() {
            if (campoDataHora.value) {
                buscarConsultasPorDia(campoDataHora.value);
            }
        });
    }
});
document.addEventListener('DOMContentLoaded', function() {
  const inputFiltro = document.getElementById('filtro-medicamento');
  const selectMedicamento = document.querySelector('select[name="medicamento"]');

  if (inputFiltro && selectMedicamento) {
    inputFiltro.addEventListener('input', function() {
      const filtro = inputFiltro.value.toLowerCase();

      Array.from(selectMedicamento.options).forEach(option => {
        // Mostra só as opções cujo texto inclui o filtro (case insensitive)
        option.style.display = option.text.toLowerCase().includes(filtro) ? 'block' : 'none';
      });
    });
  }
});