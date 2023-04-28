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
            <div class="row sidebar-buttons">
              <CCol>
                <CButton block variant="ghost" size="lg" color="light">Geral</CButton>
              </CCol>
            </div>
             
            <div class="row sidebar-buttons">
              <CCol>
                <CButton block variant="ghost"  size="lg" color="light">Parâmetros</CButton>
              </CCol>
            </div>

            <div class="row sidebar-buttons">
              <CCol>
                <CButton block variant="ghost"  size="lg" color="light">Estatísticas</CButton>
              
              </CCol>
            </div>
    
            <div class="row sidebar-buttons side-bar-config">
              <CCol>
                <CButton block variant="ghost"  size="lg" color="light">Câmeras</CButton>
              </CCol>
            </div>
            
            <div class="row sidebar-buttons side-bar-config">
              <CCol>
                <CButton block variant="ghost"  size="lg" color="light">Usuários</CButton>
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

          <div class="main-card">

            <div class="col-sm- principal">

            
               <CRow>
      <CCol>
        <CCard>
          <CCardHeader>
            <strong>Basic Form</strong> Elements
          </CCardHeader>
          <CCardBody>
            <CForm>


              <CInput
                label="Número de pessoas por m²"
                size="lg"
                placeholder="número de pessoas"
                horizontal
              />

              <template v-for="(name, key) in radioNames">
                <CRow form class="form-group" :key="name">
                  <CCol >
                    {{name}}
                  </CCol>
                  <CInputRadioGroup
                    class="col-sm-9"

                    :options="options"
                    :custom="key > 1"
                    :checked="`Option ${key}`"
                    :inline="key % 2 === 1"
                  />
                </CRow>
              </template>

              <CSelect
                label="Tempo sem mascara para notificar"
                size="lg"
                horizontal
                :value.sync="selectedOption"
                :options="selectOptions"
                placeholder="Please select"
              />

              <CSelect
                label="Tempo sem mascara para notificar"
                size="lg"
                horizontal
                :value.sync="selectedOption"
                :options="selectOptions"
                placeholder="Please select"
              />



            </CForm>

          </CCardBody>
          <CCardFooter>
            <CButton type="submit" size="sm" color="primary"><CIcon name="cil-check-circle"/> Submit</CButton>
            <CButton type="reset" size="sm" color="danger"><CIcon name="cil-ban"/> Reset</CButton>
          </CCardFooter>
        </CCard>
        
      </CCol>

            </CRow>
              </div>
            </div>
      

        </main>

      </div>

</body>    
</template>
    
    

<script>
export default {
  name: 'Forms',
  data () {
    return {
      selected: [], // Must be an array reference!
      show: true,
      horizontal: { label:'col-3', input:'col-9' },
      //Adiciona checkbox
      options: ['Obrigatório',
                'Opicional',
                ],
      selectOptions: [
          '10segundos' , '30 segundos', '1 minuto',
        { 
          value: 'some value', 
          label: 'Tempo'
        }
      ],
      selectedOption: 'some value',

      formCollapsed: true,

      radioNames: ['Uso de máscara' ]
     }
  },
  methods: {
    validator (val) {
      return val ? val.length >= 4 : false
    }
  }
}
</script>

</script>



<style>
.main {
  position: relative;
  border-top: 50px;
}

.principal {
  position: relative;
  margin-left: 20%;
}

.sidebar-buttons {
  position: relative;
  margin-top: 10%;
}

.btn-painel {
  position: relative;
  margin-top: 40%;
}


</style>