def criar_pergunta(texto_pergunta, dias):
    """
    Cria uma pergunta com o texto `texto_pergunta` e publica a
    pergunta com o número de dias `dias` em relação ao momento atual
    (número negativo para perguntas publicadas no passado, número positivo
    para perguntas que ainda serão publicadas).
    """
    tempo = timezone.now() + datetime.timedelta(days=dias)
    return Question.objects.create(question_text=texto_pergunta, pub_date=tempo)


class QuestionIndexViewTests(TestCase):
    def test_sem_perguntas(self):
        """
        Se não houver perguntas, uma mensagem apropriada será exibida.
        """
        response = self.client.get(reverse("polls:index"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Não há enquetes disponíveis.")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_pergunta_passada(self):
        """
        Perguntas com uma data de publicação no passado são exibidas na
        página inicial.
        """
        pergunta = criar_pergunta(texto_pergunta="Pergunta passada.", dias=-30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [pergunta],
        )

    def test_pergunta_futura(self):
        """
        Perguntas com uma data de publicação no futuro não são exibidas na
        página inicial.
        """
        criar_pergunta(texto_pergunta="Pergunta futura.", dias=30)
        response = self.client.get(reverse("polls:index"))
        self.assertContains(response, "Não há enquetes disponíveis.")
        self.assertQuerySetEqual(response.context["latest_question_list"], [])

    def test_pergunta_futura_e_pergunta_passada(self):
        """
        Mesmo que existam perguntas passadas e futuras, apenas as perguntas
        passadas serão exibidas.
        """
        pergunta_passada = criar_pergunta(texto_pergunta="Pergunta passada.", dias=-30)
        criar_pergunta(texto_pergunta="Pergunta futura.", dias=30)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [pergunta_passada],
        )

    def test_duas_perguntas_passadas(self):
        """
        A página de perguntas pode exibir múltiplas perguntas.
        """
        pergunta1 = criar_pergunta(texto_pergunta="Pergunta passada 1.", dias=-30)
        pergunta2 = criar_pergunta(texto_pergunta="Pergunta passada 2.", dias=-5)
        response = self.client.get(reverse("polls:index"))
        self.assertQuerySetEqual(
            response.context["latest_question_list"],
            [pergunta2, pergunta1],
        )
