<template>

<div class="container main">
  <CRow>
    
    <CCol>

      <CCard>
        <CCardHeader>
          <div class="row">
            <div class="col header-name">
          <strong>Report de Bugs</strong>
            </div>
            <div class="col in-btn">
          <CHeaderNavLink to="/dashboardSimples">  
            <CCol class="mb-3 mb-xl-0 text-center">
              <CButton color="success" size="lg" shape="pill">Voltar</CButton>
            </CCol>
          </CHeaderNavLink>
            </div>
          </div>
          
        </CCardHeader>
          <CCardBody>

              <div class="row">

                <div class="col">
                  <p>
                  Conte-nos detalhadamente qual problema ocorreu no seu sistema
                  </p>
                </div>



              </div>    

            <CForm>

              <CTextarea
                label="Bug"
                placeholder="Detalhes..."
                horizontal
                rows="9"
              />

              


              <CInputFile
                label="Print Telas de Erro"
                horizontal
                multiple
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
      options: ['Dashboard',
                'Dashboard Simples',
                'Estatisticas',
                'Cadastro de Salas', 
                'Cadastro de Usuarios', 
                'Configuracao de Parametros'
                ],
      selectOptions: [
          'Option 1', 'Option 2', 'Option 3',
        { 
          value: 'some value', 
          label: 'Selected option'
        }
      ],
      selectedOption: 'some value',

      formCollapsed: true,
      //Comentados outros tipos de Checkbox
      checkboxNames: ['Telas' 
                       //,'Inline Checkboxes', 'Checkboxes - custom', 'Inline Checkboxes - custom
                      ],
      /**                  
      RADIOS
      radioNames: ['Radios', 'Inline Radios',
                    'Radios - custom', 'Inline Radios - custom']
    */
    }
  },
  methods: {
    validator (val) {
      return val ? val.length >= 4 : false
    }
  }
}
</script>


<style>

.main{
  position: relative;
  margin-top: 5%;
  width: 100%;
}

.text-card{
  position: relative;
  width: 80%;
}

.img-card{
  position: relative;
  width: 25%;
  left: 320px;

}

.button {
  position: relative;
  left: 150px;
  bottom: 10px;
}
.header-name{
  position: relative;
  margin-top: 5%;
}

.in-btn {
  position: relative;
  margin-top: 3%;
  margin-left: 40%;
}

</style>
