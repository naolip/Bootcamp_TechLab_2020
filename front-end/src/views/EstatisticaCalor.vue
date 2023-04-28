<template>

<body class="c-app">
  
  <div class="sidebar">
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
            <div class="row sidebar-buttons">
              <CCol>
                <CHeaderNavLink class="text-decoration-none" to="/estatisticaPessoas">
                <CButton block variant="ghost" size="lg" color="light">Entrada de pessoas</CButton>
                </CHeaderNavLink>
              </CCol>
            </div>
    
            <div class="row sidebar-buttons">
              <CCol>
                <CHeaderNavLink class="text-decoration-none" to="/estatisticaCalor">
                <CButton block variant="ghost"  size="lg" color="light">Mapa de Calor</CButton>
                </CHeaderNavLink>                
              </CCol>
            </div>
    
            <div class="row sidebar-buttons">
              <CCol>
                <CHeaderNavLink class="text-decoration-none" to="/estatisticaSalas">
                <CButton block variant="ghost"  size="lg" color="light">Uso de Salas</CButton>
                </CHeaderNavLink>              
              </CCol>
            </div>
          </div> 

          <div class="row sidebar-buttons">
            <CCol>
              <CHeaderNavLink class="text-decoration-none" to="/estatisticaHistorico">
                <CButton block variant="ghost"  size="lg" color="light">Histórico</CButton>
              </CHeaderNavLink>
            </CCol>
          </div>

          <div class="row sidebar-buttons btn-painel">
            <CCol>
              <CHeaderNavLink class="text-decoration-none" to="/painelAdmin">
                <CButton block variant="ghost"  size="lg" color="light">Painel Admin</CButton>
              </CHeaderNavLink>
            </CCol>
          </div>


  </CSidebar>
  </div>

  <main class="c-main">

  <div class="container">

    <div class="principal">
  
  <CRow>
    <CCol >
      <CCard>
        <CCardHeader>
          <CIcon name="cil-justify-center"/>
          <strong> Bootstrap Carousel</strong>
          <div class="card-header-actions">
            <a 
              href="https://coreui.io/vue/docs/components/carousel" 
              class="card-header-action" 
              rel="noreferrer noopener" 
              target="_blank"
            >
              <small class="text-muted">docs</small>
            </a>
          </div>
        </CCardHeader>
        <CCardBody>
          <CCarousel
            arrows
            indicators
            animate
            height="400px"
          >

            <CCarouselItem
            image="data:image/jpeg;base64,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"
            />
          </CCarousel>
        </CCardBody>
      </CCard>
    </CCol>
  </CRow>
  

    </div>
  </div>  
  </main>
</body>
</template>

<script>
export default {
  name: 'Carousels'
}
</script>

<style>

.principal {
  position: relative;
  margin-left: 20%;
  bottom: 100px;
}

.sidebar-buttons {
  position: relative;
  margin-top: 15%;
}

.btn-painel {
  position: relative;
  margin-top: 40%;
}

</style>
