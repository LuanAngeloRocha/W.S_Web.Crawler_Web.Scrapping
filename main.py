import scrapy 

class FatecBot(scrapy.Spider):
    name = "Fatec Bot"
    urls = ["https://www.alura.com.br/cursos-online-programacao", 
    "https://www.alura.com.br/cursos-online-front-end"]

    for url in start_urls:
    
        
        def parse(self,response):
            SELETOR = ".subcategoria__item"
            cursos = []

            for categoria in response.css(SELETOR):
                curso = {}

                NOME_SELETOR = ".card-curso__nome ::text"
                LINK_SELETOR = ".card-curso ::attr(href)"

                curso['nome']= categoria.css(NOME_SELETOR).extract_first()
                curso['link']= "https://www.alura.com.br/" + categoria.css(LINK_SELETOR).extract_first()
                
                print(curso)
               

                
                
                cursos.append(curso)
            
            print("Quantidade de Cursos:", len(cursos))

        

       