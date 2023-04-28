<template>

<div class="container main">
  <CRow>
    
    <CCol>

      <CCard>
        <CCardHeader>
          <strong>VISAO DA CAMERA 1</strong>
        </CCardHeader>
          <CCardBody>

        <CCardBody>
          <CCarousel
            arrows
            indicators
            animate
            height="400px"
          >

            <CCarouselItem
            image="https://www.logitech.com/content/dam/logitech/vc/en/meeting-room-guide/meeting-room-guide-9.jpg.imgw.1000.1000.jpg"
            />
          </CCarousel>
        </CCardBody>

          </CCardBody>

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


</style>
