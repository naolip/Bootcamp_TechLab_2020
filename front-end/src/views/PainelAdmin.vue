<template>
<body class="c-app">   
  <div class="container">
    <div class="c-sidebar">
      <CSidebar 
        fixed 
        :minimize="minimize"
        :show="show"
        @update:show="(value) => $store.commit('set', ['sidebarShow', value])"
      >
        <CSidebarBrand class="d-md-down-none" to="/">
    
          <CIcon 
            class="c-sidebar-brand-full" 
            name="logo" 
            size="custom-size" 
            :height="35" 
            viewBox="0 0 556 134"
          />
    
          <CIcon 
            class="c-sidebar-brand-minimized" 
            name="logo" 
            size="custom-size" 
            :height="35" 
            viewBox="0 0 110 134"
          />
    
        </CSidebarBrand>
    
    
        <CRenderFunction flat :content-to-render="$options.nav"/>
    
        <CSidebarMinimizer
          class="d-md-down-none"
          @click.native="$store.commit('set', ['sidebarMinimize', !minimize])"
        />
    
          <div>
            <div class="row side-bar-buttons">
              <CCol>
                <CHeaderNavLink class="text-decoration-none" to="/estatisticas">
                <CButton block variant="ghost" size="lg" color="light">Estruturas</CButton>
                </CHeaderNavLink>
              </CCol>
            </div>
             
            <div class="row side-bar-buttons">
              <CCol>
              <CHeaderNavLink class="text-decoration-none" to="/estatisticaHistorico">
                <CButton block variant="ghost"  size="lg" color="light">Estatísticas</CButton>
              </CHeaderNavLink>
              </CCol>
            </div>
    
            <div class="row side-bar-buttons">
              <CCol>
                <CHeaderNavLink class="text-decoration-none" to="/cadastroUsuario">
                <CButton block variant="ghost"  size="lg" color="light">Cadastro de Usuários</CButton>
                </CHeaderNavLink>
              </CCol>
            </div>
    
            <div class="row side-bar-buttons">
              <CCol>
                <CHeaderNavLink class="text-decoration-none" to="/config">
                <CButton block variant="ghost"  size="lg" color="light">Configurações</CButton>
                </CHeaderNavLink>
              </CCol>
            </div>
          </div> 
    
      </CSidebar>
      </div>

 

        <main class="c-main">

          <div class="main-card container">
            <CCol>
              <CCard>
                <CCardHeader>
                  Maior Atividade
                  <div class="card-header-actions">
                    <a 
                      href="https://coreui.io/vue/docs/components/card-components" 
                      class="card-header-action" 
                      rel="noreferrer noopener" 
                      target="_blank"
                    >
                      <small class="text-muted">cameras</small>
                    </a>
                  </div>
                </CCardHeader>

              <div class="row">

                <div class="col">
                <CCardBody>
                  
                   <CHeaderNavLink class="text-decoration-none" to="/cameras">
                    <CCol >
                      <CWidgetProgress
                        header="SALA 1"
                        text="Capacidade"
                        footer="15/30"
                        color="warning"
                        :value="50"
                      />
                    </CCol>
                     </CHeaderNavLink>
              
                </CCardBody>

                </div>

                <div class="col">

                  <CCardBody>
                  
                    <CHeaderNavLink class="text-decoration-none" to="/cameras">
                    <CCol >
                      <CWidgetProgress
                        header="SALA 2"
                        text="Capacidade"
                        footer="0/30"
                        color="warning"
                        :value="0"
                      />
                    </CCol>
                    </CHeaderNavLink>
                  </CCardBody>
                </div>
                
                <div class="w-100"></div>
                
                <div class="col">
                 <CCardBody>
                  <CHeaderNavLink class="text-decoration-none" to="/cameras">
                    <CCol >
                      <CWidgetProgress
                        header="SALA 3"
                        text="Capacidade"
                        footer="10/40"
                        color="info"
                        :value="25"
                      />
                    </CCol>
                  </CHeaderNavLink>
                </CCardBody>
                </div>

                <div class="col">
                 <CCardBody>
                  <CHeaderNavLink class="text-decoration-none" to="/cameras">
                    <CCol >
                      <CWidgetProgress
                        header="SALA 4"
                        text="Capacidade"
                        footer="15/20"
                        color="danger"
                        :value="75"
                      />
                    </CCol>
              </CHeaderNavLink>
                </CCardBody>
                </div>

                <div class="w-100"></div>
                
                <div class="col">
                 <CCardBody>
                  <CHeaderNavLink class="text-decoration-none" to="/cameras">
                    <CCol >
                      <CWidgetProgress
                        header="SALA 5"
                        text="Capacidade"
                        footer="18/20"
                        color="danger"
                        :value="90"
                      />
                    </CCol>
              </CHeaderNavLink>
                </CCardBody>
                </div>
                <div class="col">
                 <CCardBody>
                  <CHeaderNavLink class="text-decoration-none" to="/cameras">
                    <CCol >
                      <CWidgetProgress
                        header="SALA 6"
                        text="Capacidade"
                        footer="10/40"
                        color="info"
                        :value="25"
                      />
                    </CCol>
              </CHeaderNavLink>
                </CCardBody>
                </div>
                </div>
              </CCard>
            </CCol>
          </div>

        </main>

      </div>

</body>    
</template>
    




<style>
.side-bar-buttons{
    margin-top: 25%;
    height: 50px;
  }


.main-card {
  position: relative;
  width: 100%;
}



</style>