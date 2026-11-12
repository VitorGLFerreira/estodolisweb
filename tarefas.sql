INSERT INTO tarefa (nomeTarefa, descricao, categoria,
                    dataPrazo, prioridade, status)
VALUES
('Trabalho de História', 'Capítulo 4 e resumo de 2 páginas', 'Escola', '2026-12-10', 'ALTA', 'Pendente'),
('Trabalho de Português', 'Verbos no passado', 'Escola', '2026-11-26', 'MEDIA', 'Pendente'),
('Estudar para Matemática', 'Equações de 2º grau e exercícios', 'Escola', '2026-11-28', 'ALTA', 'Pendente'),
('Projeto de Ciências', 'Pesquisa sobre ecossistemas', 'Escola', '2026-12-05', 'BAIXA', 'Pendente'),
('Leitura de Inglês', 'Capítulo 2 do livro', 'Escola', '2026-12-02', 'MEDIA', 'Pendente');

SELECT * FROM tarefa;