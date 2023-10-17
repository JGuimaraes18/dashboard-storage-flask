import plotly.express  as  px 
import pandas as pd

dfAggOlinda = ''
dfAggLandsat = ''
# dfAggAmazonia = ''

def generate_html_Agg(dataframeOlinda: dfAggOlinda, dataframeLandsat: dfAggLandsat, capacityLiqOlinda, appTipoS_volOlinda, capacityUsadoOlinda, appTipoUnidadeOlinda, percentUsedConvertedOlinda,capacityDisponivelOlinda, appTipoUnidadeDispoOlinda, percentDispoConvertedOlinda, appConTotalS_volOlinda, appConTotalS_snapOlinda, appTipoS_snapOlinda, appConTotalU_volOlinda, appTipoU_volOlinda, appConTotalU_snapOlinda, appTipoU_snapOlinda, usedTotalOlinda, dispoTotalOlinda, capacityLiqLandsat, capacityUsadoLandsat, percentUsedConvertedLandsat, capacityDisponivelLandsat, percentDispoConvertedLandsat, usedTotalLandsat, dispoTotalLandsat, appTipoUnidadeLandsat, appTipoUnidadeDispoLandsat, appConTotalS_volLandsat, appConTotalU_volLandsat, appTipoS_volLandsat, appTipoU_volLandsat, appConTotalS_snapLandsat, appConTotalU_snapLandsat, appTipoU_snapLandsat, appTipoS_snapLandsat, appConTotalS_volAmazonia, appConTotalU_volAmazonia, appTipoS_volAmazonia, appTipoU_volAmazonia, appConTotalS_snapAmazonia, appConTotalU_snapAmazonia, appTipoS_snapAmazonia, appTipoU_snapAmazonia):

# def generate_html_Agg(dataframeOlinda: dfAggOlinda, dataframeLandsat: dfAggLandsat, dataframeAmazonia: dfAggAmazonia,capacityLiqOlinda, appTipoS_volOlinda, capacityUsadoOlinda, appTipoUnidadeOlinda, percentUsedConvertedOlinda,capacityDisponivelOlinda, appTipoUnidadeDispoOlinda, percentDispoConvertedOlinda, appConTotalS_volOlinda, appConTotalS_snapOlinda, appTipoS_snapOlinda, appConTotalU_volOlinda, appTipoU_volOlinda, appConTotalU_snapOlinda, appTipoU_snapOlinda, usedTotalOlinda, dispoTotalOlinda, capacityLiqLandsat, capacityUsadoLandsat, percentUsedConvertedLandsat, capacityDisponivelLandsat, percentDispoConvertedLandsat, usedTotalLandsat, dispoTotalLandsat, appTipoUnidadeLandsat, appTipoUnidadeDispoLandsat, capacityLiqAmazonia, capacityUsadoAmazonia, percentUsedConvertedAmazonia, capacityDisponivelAmazonia, percentDispoConvertedAmazonia,  usedTotalAmazonia, dispoTotalAmazonia, appTipoUnidadeAmazonia, appTipoUnidadeDispoAmazonia, appConTotalS_volLandsat, appConTotalU_volLandsat, appTipoS_volLandsat, appTipoU_volLandsat, appConTotalS_snapLandsat, appConTotalU_snapLandsat, appTipoU_snapLandsat, appTipoS_snapLandsat, appConTotalS_volAmazonia, appConTotalU_volAmazonia, appTipoS_volAmazonia, appTipoU_volAmazonia, appConTotalS_snapAmazonia, appConTotalU_snapAmazonia, appTipoS_snapAmazonia, appTipoU_snapAmazonia):

  
    table_html_Olinda = dataframeOlinda.to_html(table_id="table-Olinda")
    table_html_Landsat = dataframeLandsat.to_html(table_id="table-Landsat")
    # table_html_Amazonia = dataframeAmazonia.to_html(table_id="table-Amazonia")
  
    # chart_Olinda = px.pie(values=[usedTotalOlinda, dispoTotalOlinda], names=['usado', 'disponivel'], color_discrete_sequence=px.colors.qualitative.Light24)

    # # chart_Olinda.write_image('teste.png')
    
    # teste = chart_A
    
    html_Agg = f"""
    <html>
    <header>
        <link href="https://cdn.datatables.net/1.11.5/css/jquery.dataTables.min.css" rel="stylesheet">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
        <link rel="stylesheet" href="https://cdngovbr-ds.estaleiro.serpro.gov.br/design-system/fonts/rawline/css/rawline.css"/>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.11.2/css/all.min.css"/>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Anton&display=swap" rel="stylesheet">
        <link rel="stylesheet" type="text/css" href="static/css/armazenamento.css"/>
        <link rel="stylesheet" type="text/css" href="static/css/footer.css"/>
        <title>Armazenamento</title>
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
    
    <div class="page-content">  
    
    <div class="container conteudo-coids">

  <h1 class="text-center subtitulo-padrao-conteudo">OLINDA</h1> 

  <div class="accordion accordion-flush" id="accordionFlushExample">
    <div class="accordion-item fonte-accordion">
      <h2 class="accordion-header" id="flush-headingOne">
        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapseOne" aria-expanded="false" aria-controls="flush-collapseOne">
          <h4>Armazenamento</h4>
        </button>
      </h2>
      <div id="flush-collapseOne" class="accordion-collapse collapse" aria-labelledby="flush-headingOne" data-bs-parent="#accordionFlushExample">
        <div class="accordion-body">
          <div class="row d-flex align-items-center">
            &nbsp;
            {table_html_Olinda}
            &nbsp;
          
  
          <div class="box__content__arm col-md-6 d-flex flex-column texto-padrao-conteudo">
            <p>
            <strong>Total Aggregates:</strong> &nbsp;{ capacityLiqOlinda }&nbsp;{appTipoS_volOlinda}
            </p>
            <p>
            <strong>Utilizado:</strong> &nbsp;{ capacityUsadoOlinda }&nbsp;{appTipoUnidadeOlinda}&nbsp;-&nbsp; {percentUsedConvertedOlinda}%
            </p>
            <p>
            <strong>      Disponível:</strong> &nbsp;{ capacityDisponivelOlinda }&nbsp;{appTipoUnidadeDispoOlinda}&nbsp;-&nbsp; {percentDispoConvertedOlinda }%
            </p>
          </div>
          <div class="chart-storage col-md-3 d-flex flex-row-reverse">
              {{% include 'graficoStorageOlinda.html' %}}
          </div>
        </div>
         </div>
       </div>
    </div>
    <div class="accordion-item fonte-accordion">
      <h2 class="accordion-header" id="flush-headingTwo">
        <button class="accordion-button collapsed fonte-accordion" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapseTwo" aria-expanded="false" aria-controls="flush-collapseTwo">
          <h4>Volumes</h4>
        </button>
      </h2>
      <div id="flush-collapseTwo" class="accordion-collapse collapse" aria-labelledby="flush-headingTwo" data-bs-parent="#accordionFlushExample">
        <div class="accordion-body">
          <div class="texto-padrao-conteudo">
            <p>
            <strong>Total:</strong> &nbsp; {appConTotalS_volOlinda}&nbsp;{appTipoS_volOlinda}
            | <strong>Snaps:</strong>&nbsp;{appConTotalS_snapOlinda}&nbsp;{appTipoS_snapOlinda}
            </p>
            </div>
            <div class="texto-padrao-conteudo">
              <p>
              <strong>Utilizado:</strong> &nbsp; {appConTotalU_volOlinda}&nbsp;{appTipoU_volOlinda}
            | <strong>Snaps:</strong>&nbsp;{appConTotalU_snapOlinda}&nbsp;{appTipoU_snapOlinda}
              </p>
              <!--
              <div class="chart-vol">
                {{% include 'graficoVolumesOlinda.html' %}}
              </div>
              -->
            &nbsp;
          </div>
        </div>
      </div>
    </div>
  </div>
  
  <h1 class="text-center subtitulo-padrao-conteudo">Landsat</h1> 

  <div class="accordion accordion-flush" id="accordionFlushExample">
    <div class="accordion-item fonte-accordion">
      <h2 class="accordion-header" id="flush-headingThree">
        <button class="accordion-button collapsed" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapseThree" aria-expanded="false" aria-controls="flush-collapseThree">
          <h4>Armazenamento</h4>
        </button>
      </h2>
      <div id="flush-collapseThree" class="accordion-collapse collapse" aria-labelledby="flush-headingOThree" data-bs-parent="#accordionFlushExample">
        <div class="accordion-body">
          <div class="row d-flex align-items-center">
            <div class="box__content__arm col-md-6 d-flex flex-column texto-padrao-conteudo">
              <p>
            <strong>Capacidade Líquida:</strong> &nbsp;{ capacityLiqLandsat }&nbsp;{appTipoS_volLandsat}
              </p>
            <p>
            <strong>Utilizado:</strong> &nbsp;{ capacityUsadoLandsat }&nbsp;{appTipoUnidadeLandsat}&nbsp;-&nbsp; {percentUsedConvertedLandsat}%
            </p>
            <p>
            <strong>Disponível:</strong> &nbsp;{ capacityDisponivelLandsat }&nbsp;{appTipoUnidadeDispoLandsat}&nbsp;-&nbsp; {percentDispoConvertedLandsat }%
            </p>
            </div>
            <div class="chart-storage col-md-6 d-flex flex-row-reverse">
              {{% include 'graficoStorageLandsat.html' %}}
            </div>
            &nbsp;
          </div>
          <div class="container table_aggregates">
          <h1 class="text-center subtitulo-padrao-conteudo">Aggregates</h1> 
          {table_html_Landsat}
        </div>
          
        </div>
      </div>
    </div>
    <div class="accordion-item fonte-accordion">
      <h2 class="accordion-header" id="flush-headingFour">
        <button class="accordion-button collapsed fonte-accordion" type="button" data-bs-toggle="collapse" data-bs-target="#flush-collapseFour" aria-expanded="false" aria-controls="flush-collapseFour">
          <h4>Volumes</h4>
        </button>
      </h2>
      <div id="flush-collapseFour" class="accordion-collapse collapse" aria-labelledby="flush-headingFour" data-bs-parent="#accordionFlushExample">
        <div class="accordion-body">
          <div class="texto-padrao-conteudo">
            <p>
            <strong>Total:</strong> &nbsp; {appConTotalS_volLandsat}&nbsp;{appTipoS_volLandsat}
            | <strong>Snaps:</strong>&nbsp;{appConTotalS_snapLandsat}&nbsp;{appTipoS_snapLandsat}
            </p>
            </div>
            <div class="texto-padrao-conteudo">
              <p>
              <strong>Utilizado:</strong> &nbsp; {appConTotalU_volLandsat}&nbsp;{appTipoU_volLandsat}
            | <strong>Snaps:</strong>&nbsp;{appConTotalU_snapLandsat}&nbsp;{appTipoU_snapLandsat}
              </p>
          </div>
        </div>
      </div>
    </div>
  </div>

</div>
        
    
        <!-- Footer -->
  <footer class="text-center text-lg-start fundo-escuro" id="footer">

    <!-- Section: Links  -->
    <section class="p-4">
      <div class="container text-center text-md-start mt-5">
        <!-- Grid row -->
        <div class="row mt-3">
          <!-- Grid column -->
          <div class="col-md-3 col-lg-4 col-xl-3 mx-auto mb-4">
            <!-- Content -->
            <h6 class="text-uppercase fw-bold mb-4">
              <div class="footer">
                <a class="navbar-brand header-logo text-light d-flex align-items-center" href="http://condado.cptec.inpe.br/site-gov-coids/index.html" id="footer">
                  <img src="static/img/logo_COIDS_GRANDE-PhotoRoom.png" id="logo-coids" class="img-fluid"
                    alt="logo-coids" />
                  <h1>COIDS</h1>
                </a>
                <a class="navbar-brand header-logo text-light d-flex align-items-center mt-3"
                  href="https://www.gov.br/inpe/pt-br" target="_blank">
                  <img src="static/img/inpe_logo2023" id="logo-inpe" class="img-fluid" alt="logo-inpe" />
                </a>
              </div>
            </h6>
          </div>
          <!-- Grid column -->

          <!-- Grid column -->
          <div class="col-md-2 col-lg-2 col-xl-2 mx-auto mb-4 fonte_footer">
            <!-- Links -->
            <h6 class="text-uppercase fw-bold mb-4 titulo_footer">
              Serviços
            </h6>

            <p>
              <a class="text-reset" href="http://sssn.cptec.inpe.br/" target="_blank">3S Portal</a>
            </p>
            <p>
              <a href="http://condado:8000/" class="text-reset" target="_blank">Netbox</a>
            </p>
            <p>
              <a href="http://mansidao.cptec.inpe.br/wiki/" class="text-reset" target="_blank">Wiki</a>
            </p>
            <p>
              <a href="http://juazeiro.cptec.inpe.br/ocomon_coids/login.php" class="text-reset"
                target="_blank">Racktables</a>
            </p>
          </div>
          <!-- Grid column -->

          <!-- Grid column -->
          <div class="col-md-3 col-lg-2 col-xl-2 mx-auto mb-4 fonte_footer">
            <!-- Links -->
            <h6 class="text-uppercase fw-bold mb-4 titulo_footer">
              Estatísticas
            </h6>
            <p>
              <a href="http://condado.cptec.inpe.br/site-gov-coids/estatisticas.html" class="text-reset">Aplicações</a>
            </p>
            <p>
              <a href="http://condado.cptec.inpe.br/site-gov-coids/estatisticas.html" class="text-reset">Downloads</a>
            </p>
          </div>
          <!-- Grid column -->

          <!-- Grid column -->
          <div class="col-md-3 col-lg-2 col-xl-2 mx-auto mb-4 fonte_footer">
            <!-- Links -->
            <h6 class="text-uppercase fw-bold mb-4 titulo_footer">
              Contato
            </h6>
            <p>
              <a href="http://condado.cptec.inpe.br/site-gov-coids/contato.html" class="text-reset">Secretaria</a>
            </p>
          </div>
          <!-- Grid column -->

          <!-- Grid column -->
          <div class="col-md-4 col-lg-3 col-xl-3 mx-auto mb-md-0 mb-4 fonte_footer">
            <!-- Links -->
            <h6 class="text-uppercase fw-bold mb-4">Sobre</h6>
            <p>
              <a href="http://condado.cptec.inpe.br/site-gov-coids/sobre.html" class="text-reset">A COIDS</a>
            </p>
          </div>
          <!-- Grid column -->
        </div>
        <!-- Grid row -->
      </div>
    </section>
    <!-- Section: Links  -->

    <!-- Copyright -->
    <div class="container">
      <div class="text-center p-4 d-flex fonte-footer" style="background-color: rgba(0, 0, 0, 0.05);">
        <div class="col-6 text-medium">2023 © COIDS - Coordenação de Infraestrutura de Dados e Supercomputação</div>
        <div class="col-6 text-medium">Desenvolvimento: COIDS/WEB</div>
      </div>
    </div>
    <!-- Copyright -->
  </footer>
  <!-- Footer -->
    </div>
    
    
    <!-- JavaScript Bundle with Popper -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/js/bootstrap.bundle.min.js" integrity="sha384-OERcA2EqjJCMA+/3y+gxIOqMEjwtxJY7qPCqsdltbNJuaOe923+mo//f6V8Qbsw3" crossorigin="anonymous"></script>
<!--<script src="./static/js/controller.js"></script>-->
<script src="https://code.jquery.com/jquery-3.5.1.slim.min.js"
  integrity="sha384-DfXdz2htPH0lsSSs5nCTpuj/zy4C+OGpamoFVy38MVBnE+IbbVYUew+OrCXaRkfj" crossorigin="anonymous"></script>
<script src="https://cdn.jsdelivr.net/npm/popper.js@1.16.1/dist/umd/popper.min.js"
  integrity="sha384-9/reFTGAW83EW2RDu2S0VKaIzap3H66lZH81PoYlFhbGU+6BZp6G7niu735Sk7lN" crossorigin="anonymous"></script>
<script src="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/js/bootstrap.min.js"
  integrity="sha384-B4gt1jrGC7Jh4AgTPSdUtOBvfO8shuf57BaghqFfPlYxofvL8/KUEfYiJOMMV+rV" crossorigin="anonymous"></script>
    <script src="https://code.jquery.com/jquery-3.6.0.slim.min.js" integrity="sha256-u7e5khyithlIdTpu22PHhENmPcRdFiHRjhAuHcs05RI=" crossorigin="anonymous"></script>
    <script type="text/javascript" src="https://cdn.datatables.net/1.11.5/js/jquery.dataTables.min.js"></script>
    <script>
        $(document).ready( function () {{
            $('#table-Olinda').DataTable({{
                pageLength: 25
            }});
        }});
        $(document).ready( function () {{
            $('#table-Landsat').DataTable({{
                pageLength: 25
            }});
        }});
        $(document).ready( function () {{
            $('#table-Amazonia').DataTable({{
                pageLength: 25
            }});
        }});
        
    </script>
    
    </body>
    </html>
    """
    return html_Agg