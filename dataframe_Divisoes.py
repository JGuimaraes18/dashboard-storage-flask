df_D = ''
df_Geral_Agg = ''
def generate_html_D(dataframe: df_D, divOlinda, mergeTotalDivOlinda, mergeUsadoDivOlinda, mergeDisponivelDivOlinda):
    tableid = 'table-' + divOlinda
    table_html_D = dataframe.to_html(table_id=tableid)
    html_d = f"""

    <header>
           <meta charset="UTF-8" />
    
    <!-- CSS only -->

    <link href="https://cdn.datatables.net/1.11.5/css/jquery.dataTables.min.css" rel="stylesheet">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdngovbr-ds.estaleiro.serpro.gov.br/design-system/fonts/rawline/css/rawline.css"/>
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.11.2/css/all.min.css"/>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Anton&display=swap" rel="stylesheet">
    <link rel="stylesheet" type="text/css" href="static/css/divisoes.css"/>
    </header>

    <div class="accordion accordion-flush" id="{divOlinda}">
        <div class="accordion-item fonte-accordion" >
            <h2 class="accordion-header" id="{divOlinda}">
                <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#{divOlinda}" aria-expanded="false" aria-controls="{divOlinda}">
                    <h4>{divOlinda}</h4>
                </button>
            </h2>

            <div id="{divOlinda}" class="accordion-collapse collapse" aria-labelledby="{divOlinda}" data-bs-parent="#{divOlinda}">
                <div class="accordion-body">
                    <div class="row d-flex align-items-center">
                        <div class="col-md-12 flex-column align-items-center texto-padrao-conteudo">
                           <div class="table_unidadeOrganizacional">
                        
                            {table_html_D}

                            </div>
                            
                            <h4 class="text-center ">
                            <strong>
                            <p>Total Volumes: {mergeTotalDivOlinda}</p>                                        
                            <p>Utilizado:  {mergeUsadoDivOlinda}</p>                                        
                            <p>Disponível: {mergeDisponivelDivOlinda} </p>
                            </strong>

                        </div>   
                    </div>    
                </div> 
            </div>
        </div>     
    </div>


    <!-- JavaScript Bundle with Popper -->
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3" crossorigin="anonymous"></script>

     <script src="https://code.jquery.com/jquery-3.5.1.slim.min.js" integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>

    <script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js" integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>

    <script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js" integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>
     
    <script src="https://code.jquery.com/jquery-3.6.0.slim.min.js" integrity="sha256-u7e5khyithlIdTpu22PHhENmPcRdFiHRjhAuHcs05RI=" crossorigin="anonymous"></script>
    <script type="text/javascript" src="https://cdn.datatables.net/1.11.5/js/jquery.dataTables.min.js"></script>
    
    
    
    <script>
        $(document).ready( function () {{
            $('#{tableid}').DataTable({{
                pageLength: 15
            }});
        }});
    </script>
    """
    return html_d

def generate_html_G(dataframe: df_Geral_Agg, arrayGeralDivOlinda, exibeTotalOlinda, exibeUsadoOlinda, exibeDisponivelOlinda, TotalAggregate, UsedAggregate, DispoAggregate, percentUsedConvertedOlinda, percentDispoConvertedOlinda):
    table_html_G = dataframe.to_html(table_id="table-div")

    html_d = f"""

    <html>
    <header>
        <link href="https://cdn.datatables.net/1.11.5/css/jquery.dataTables.min.css" rel="stylesheet">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
        <link rel="stylesheet" href="https://cdngovbr-ds.estaleiro.serpro.gov.br/design-system/fonts/rawline/css/rawline.css"/>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.11.2/css/all.min.css"/>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Anton&display=swap" rel="stylesheet">
        <link rel="stylesheet" type="text/css" href="static/css/divisoes.css"/>
        <link rel="stylesheet" type="text/css" href="static/css/footer.css"/>
        <title>Organização</title>
    </header>
    <body>
    <nav class="navbar" id="header">
        <div class="container" id="bloco-lg">
            <a class="navbar-brand header-logo text-light d-flex align-items-center" href="/">
                <img src="/static/img/logo_COIDS_GRANDE.png" id="logo__coids" class="img-fluid" alt="logo__coids"/>
                <h1>COIDS</h1>
            </a>
            <div class="br-list w-30">
                <a class="br-item" id="menu__header" href="http://condado.cptec.inpe.br/site-gov-coids/index.html#header">Home</a>
                <a class="br-item" id="menu__header" href="http://condado.cptec.inpe.br/site-gov-coids/servicos.html">Serviços</a>
                <a class="br-item" id="menu__header" href="http://condado.cptec.inpe.br/site-gov-coids/estatisticas.html">Estatísticas</a>
                <a class="br-item" id="menu__header" href="http://condado.cptec.inpe.br/site-gov-coids/contato.html">Contato</a>
                <a class="br-item" id="menu__header" href="http://condado.cptec.inpe.br/site-gov-coids/sobre.html">Sobre</a>
            </div>

            <div class="col-12">
                <div class="titulo_header">
                Coordenação de Infraestrutura de Dados <br> e Supercomputação
                </div>
            </div>
        </div>
    </nav>


       <!-- container para ajuste de layout -->
      <div class="container">
  
        <div class="conteudo-coids">
<!--            <div class="accordion accordion-flush" id="accordionFlushExample">-->
                    <!--<div class="accordion-item fonte-accordion">-->
                        <div class="row d-flex align-items-center">
                            <div class="col-md-12 d-flex flex-column texto-padrao-conteudo">
                                <h3 class="text-center"><strong><p>OLINDA</p></strong></h3>
                                <h3 class="text-center"><strong><p>Aggregates</p></strong></h3>&nbsp;
                                {table_html_G}
                                &nbsp;&nbsp;
                                
                                <div class="box__content__arm col-md-12 d-flex flex-column text-center texto-padrao-conteudo">                            
                                    <div class="chart-storage col-md-3 d-flex flex-row-reverse">
                                        <div style="margin-left: -240%;"> 
                                            {{% include 'graficoStorageOlinda.html' %}} 
                                        </div>
                                        <div style="width:500px; float: center; margin-left: -100%; margin-top: 0%;">
                                            <h4 class="text-md-start"><p>Total Líquido: { TotalAggregate }</p></h4>
                                            <h4 class="text-md-start"><p>Total Usado: { UsedAggregate }  &nbsp;-&nbsp; {percentUsedConvertedOlinda}%</p></h4>
                                            <h4 class="text-md-start"><p>Total Disponível: { DispoAggregate } &nbsp;-&nbsp; {percentDispoConvertedOlinda}%</h4>
                                        </div>
                                    </div>
                                </div>
                            </div>
                        </div>
                        <!--
                        <div class="col-md-12 d-flex flex-column texto-padrao-conteudo">
                            <h3 class="text-center"><strong><p>Volumes</p></strong></h3>&nbsp;
                            <h4 class="text-md-start"><p>Total Volumes: { exibeTotalOlinda }</p></h4>&nbsp;
                            <h4 class="text-md-start"><p>Total Usado: { exibeUsadoOlinda }</p></h4>&nbsp;
                            <h4 class="text-md-start"><p>Total Disponível: { exibeDisponivelOlinda }</p></h4>&nbsp;
                        </div>
                        -->
                        &nbsp;&nbsp;

                        <div class="col-md-12 d-flex flex-column texto-padrao-conteudo">
                        <h3 class="text-center"><strong><p>Unidade Organizacional</p></strong></h3>&nbsp;

                                            {{% include 'teste.html' %}}

                        
                        </div>
                     <!--</div>-->
                  <!--</div>-->
              </div>
          </div>
  
  
        
  
        <!-- Fim do container -->
      </div>
  
    </main>
    <script src="https://code.jquery.com/jquery-3.6.0.slim.min.js" integrity="sha256-u7e5khyithlIdTpu22PHhENmPcRdFiHRjhAuHcs05RI=" crossorigin="anonymous"></script>
    <script type="text/javascript" src="https://cdn.datatables.net/1.11.5/js/jquery.dataTables.min.js"></script>
    <script>
        $(document).ready( function () {{
            $('#table-div').DataTable({{
                pageLength: 25
            }});
        }});
    </script>



    
    """
    return html_d
