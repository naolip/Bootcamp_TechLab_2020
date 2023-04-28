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
          </div> 



  </CSidebar>
  </div>

  <main class="c-main">

  <div class="container">

    <div class="principal">
   <template>
  <CChartLine
    :datasets="defaultDatasets"
    labels="months"
  />
  </template>


    </div>
  </div>  
  </main>
</body>
</template>

<script>
import { CChartLine } from '@coreui/vue-chartjs'

export default {
  name: 'CChartLineExample',
  components: { CChartLine },
  computed: {
    defaultDatasets () {
      return [
        {
          label: 'Com mascara',
          backgroundColor: 'rgb(228,102,81,0.9)',
          data: [30, 39, 10, 50, 30, 70, 35]
        },
        {
          label: 'Sem mascara',
          backgroundColor: 'rgb(0,216,255,0.9)',
          data: [39, 80, 40, 35, 40, 20, 45]
        }
      ]
    }
  }
}
</script>

<style>

.principal {
  position: relative;
  margin-top: 10%;
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
