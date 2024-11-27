from django.http import HttpResponse


def index(request):
    return HttpResponse("Olá, mundo. Você está no índice de pesquisas.")
def detail(request, question_id):
    return HttpResponse("Você está olhando para a pergunta  %s." % question_id)
def results(request, question_id):
    response = "Você está vendo os resultados da pergunta %s."
    return HttpResponse(response % question_id)
def vote(request,question_id):
    return HttpResponse("Você está votando na pergunta %s."% question_id)
