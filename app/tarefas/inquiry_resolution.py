import logging
from crewai import Task
from app.agentes.support_agent import support_agent
from crewai_tools import ScrapeWebsiteTool

docs_scrape_tool = ScrapeWebsiteTool(
    website_url="https://docs.crewai.com/how-to/Creating-a-Crew-and-kick-it-off/"
)

inquiry_resolution = Task(
    description=(
        "{customer} acabou de entrar em contato com uma pergunta muito importante:\n"
        "{inquiry}\n\n"
        "{person} de {customer} é quem entrou em contato."
        "Certifique-se de usar tudo o que você sabe"
        "para fornecer o melhor suporte possível."
        "Você deve se esforçar para fornecer uma "
        "resposta precisa à consulta do cliente."
    ),
    expected_output=(
        "Uma resposta detalhada e informativa à"
        "consulta do cliente que aborda"
        "todos os aspectos da pergunta.\n"
        "A resposta deve incluir referências"
        "para tudo que você usou para encontrar a resposta,"
        "incluindo dados ou soluções externas."
        "Certifique-se de que a resposta esteja completa,"
        "não deixando perguntas sem resposta e mantendo uma atitude prestativa e amigável"
        "tom por toda parte."
    ),
    tools=[docs_scrape_tool],
    agent=support_agent,
)

logging.info("Tarefa de resolução de consulta inicializada")
