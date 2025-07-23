from utils import iniciar_navegador, salvar_planilha
from infojobs import executar_infojobs
from indeed import executar_indeed

def main():
    # Executar fluxo InfoJobs
    detalhes_infojobs = executar_infojobs()
    salvar_planilha(detalhes_infojobs, "infojobs_detalhes.xlsx")

    # Executar fluxo Indeed (aqui você completa depois)
    detalhes_indeed = executar_indeed()
    if detalhes_indeed is not None:
        salvar_planilha(detalhes_indeed, "indeed_detalhes.xlsx")

if __name__ == "__main__":
    main()
