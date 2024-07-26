import logging
from crewai import Task
from app.agentes.support_quality_assurance_agent import support_quality_assurance_agent

quality_assurance_review = Task(
    description=(
        "Revise a resposta redigida pelo representante de suporte sênior para a consulta do {customer}."
        "Certifique-se de que a resposta seja abrangente, precisa e esteja de acordo com as "
        "padrões de alta qualidade esperados para suporte ao cliente.\n"
        "Verifique se todas as partes da consulta do cliente"
        "foram abordados"
        "completamente, com um tom útil e amigável.\n"
        "Verifique as referências e fontes usadas para"
        "encontre a informação"
        "garantir que a resposta seja bem apoiada e"
        "não deixa perguntas sem resposta."
    ),
    expected_output=(
        "Uma resposta final, detalhada e informativa"
        "pronto para ser enviado ao cliente.\n"
        "Esta resposta deve abordar totalmente o"
        "consulta do cliente, incorporando todos"
        "feedback e melhorias relevantes.\n"
        "Não seja muito formal, somos uma empresa tranquila e descolada"
        "mas mantenha um tom profissional e amigável o tempo todo."
    ),
    agent=support_quality_assurance_agent,
)

logging.info("Tarefa de revisão de garantia de qualidade inicializada")
