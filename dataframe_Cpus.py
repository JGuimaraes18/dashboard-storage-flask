df_Cpus = ''
def generate_html_Cpus(dataframe: df_Cpus):
    html_Cpus = f"""
    <html>
    <header>
        <link href="https://cdn.datatables.net/1.11.5/css/jquery.dataTables.min.css" rel="stylesheet">
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-Zenh87qX5JnK2Jl0vWa8Ck2rdkQ2Bzep5IDxbcnCeuOxjzrPF/et3URy9Bv1WTRi" crossorigin="anonymous">
        <link rel="stylesheet" href="https://cdngovbr-ds.estaleiro.serpro.gov.br/design-system/fonts/rawline/css/rawline.css"/>
        <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/5.11.2/css/all.min.css"/>
        <link rel="preconnect" href="https://fonts.googleapis.com">
        <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
        <link href="https://fonts.googleapis.com/css2?family=Anton&display=swap" rel="stylesheet">
        <link rel="stylesheet" type="text/css" href="static/css/graficos_recursos.css"/>
        <link rel="stylesheet" type="text/css" href="static/css/footer.css"/>
        <title>Recursos Computacionais</title>
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
        <div class="container conteudo-grafico">
          <h1 class="text-center subtitulo-padrao-conteudo">CPU</h1> 
          {{% include 'nCPUHost_somatoriaVMs.html' %}}
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
    
    
    <script src="https://code.jquery.com/jquery-3.6.0.slim.min.js" integrity="sha256-u7e5khyithlIdTpu22PHhENmPcRdFiHRjhAuHcs05RI=" crossorigin="anonymous"></script>
    <script type="text/javascript" src="https://cdn.datatables.net/1.11.5/js/jquery.dataTables.min.js"></script>
    <script>
        $(document).ready( function () {{
            $('#s').DataTable({{
                // paging: false,    
                // scrollY: 400,
            }});
        }});
    </script>
    
    </body>
    </html>
    """
    return html_Cpus