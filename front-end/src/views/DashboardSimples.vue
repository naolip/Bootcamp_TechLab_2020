<template>

<body class="c-app">
  
  

  <main class="c-main">
    
    <div class="container">
   
      <div class="row">

        <div class="col main-card">
          <CCol>
            <CCard>
              <CCardHeader>
                <img src="data:image/png;base64, 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" max width="100px" class="rounded mx-auto d-block header-img" alt="logo">

            <div>
              <CDropdown
                class="float-right w-75 button-drop" 
                placement="bottom-start"
                color="link"
                size="lg"
                :caret="false"
              >
                <template #toggler-content>
                           <CIcon 
          name="cil-bell"
          size="custom-size" 
          :height="20" 

          /> 
                  
                </template>
              
              <CCardHeader>
          <CBadge 
            color="danger" 
            class="float-right"> 2

          </CBadge>

          <CIcon 
          class="alert-icon"
          name="cil-bell"
          size="custom-size" 
          :height="20" 

          /> 
          <large class="alert-txt">Alertas</large>
          
        </CCardHeader>
        <CCardBody>

          <CAlert
            color="secondary"
            closeButton
            :show.sync="alert1"> 
            Detectada pessoa sem máscara!<!--{{this.alert.text-alert}}
          <CProgress
                color="danger"
                :max="dismissSecs"
                :value="dismissCountDown"
                height="4px"
          />-->
          </CAlert>

          <CAlert
            color="secondary"
            closeButton
            :show.sync="alert1">
              Pessoa sem máscara na Sala de Reuniões 2
          </CAlert>


        </CCardBody>
              </CDropdown>
           </div>
          
                
 <!--              
                  <CDropdown 
                  
                  color="transparent p-0"  
                  name="cil-settings" 
                  class="float-right w-75 button-drop" 
                  placement="bottom-start">

                    
          <CIcon 
          name="cil-bell"
          size="custom-size" 
          :height="20" 

          /> 
          


        <CCardHeader>
          <CBadge 
            color="danger" 
            class="float-right"> 2

          </CBadge>

          <CIcon 
          name="cil-bell"
          size="custom-size" 
          :height="20" 

          /> 
          <large>Alertas</large>
          <small>dismissible</small> 
        </CCardHeader>
        <CCardBody>

          <CAlert
            color="secondary"
            closeButton
            :show.sync="alert1"> {{this.alert.name}}
          <CProgress
                color="danger"
                :max="dismissSecs"
                :value="dismissCountDown"
                height="4px"
          />
          </CAlert>

          <CAlert
            color="secondary"
            closeButton
            :show.sync="alert1">
              Pessoa sem máscara na Sala de Reuniões 2
          </CAlert>


        </CCardBody>

                  </CDropdown>
                -->
              </CCardHeader>
              
              <CCardBody>

                <div class="col cards-container">  
                  <CRow>
                    <div class="col">
                      <CCol class="cards nhover" >
                        <CWidgetProgress
                          header="Total Pessoas"
                          text="Numero total de pessoas nas dependencias"
                          footer="Total: 73   Permitido: 100"
                          class="card-header-action position-relative"
                          style="right:5px; top:5px"
                          color="warning"
                          :value="73"
                        />
                      </CCol>
                    </div>
                    
                    <div class="w-100"></div>
                    
                    <div class="col">
                      <CCol class="cards nhover" >
                        <CWidgetProgress
                          header="Uso de Máscara"
                          text="Porcentagem de pessoas com máscara"
                          footer="97% Pessoas com mascara"
                          class="card-header-action position-relative"
                          
                          color="success"
                          :value="97"
                        />
                      </CCol>
                    </div>
        
                    <div class="w-100"></div>

                    <div class="col card-3">  
                      <CCol class="cards" col="12" >
                        <CWidgetIcon
                            header="Salas Livres"
                            text="10"
                            color="info"
                          >
                          <CIcon name="cil-laptop" width="24"/>
                        </CWidgetIcon>
                      </CCol>
                    </div>

                    <div class="w-100"></div>
                    
                    <div class="col card-4">
                      <CCol class="cards" col="12" >
                        <CWidgetIcon
                          header="Salas Ocupadas"
                          text="3"
                          color="danger"
                        >
                          <CIcon name="cil-bell" width="24"/>
                        </CWidgetIcon>
                      </CCol>
                    </div>
                  </CRow>  
                </div>

              </CCardBody>
            </CCard>
          </CCol>
        </div>

   


    </div> 
    
      <div class="row buttons">
          <div class="col bug-button">
            <CCol sm xs="12"  class="text-center mt-3">
              <CHeaderNavLink to="/bugReport">
                <CButton color="danger" shape="pill" variant="ghost" @click="change_state">
                  <CIcon name="cil-lightbulb"/>&nbsp;Bug Report
                </CButton>
              </CHeaderNavLink>
            </CCol>
          </div>
 <!-- 
          <div class="col dashboard-button">  
            <CHeaderNavLink to="/painelAdmin"> 
              <CCol xs=12 class="text-center mt-3">
                <CButton block color="success" shape="pill">Painel Admin</CButton>    
              </CCol>
            </CHeaderNavLink>
          </div>
-->      
      </div>

    </div> 

  </main>

</body>

</template>



<script>
import MainChartExample from './charts/MainChartExample'
import WidgetsDropdown from './widgets/WidgetsDropdown'
import WidgetsBrand from './widgets/WidgetsBrand'
import CoreUIIcons from './icons/CoreUIIcons'
import axios from 'axios'
import { cilBell } from '@coreui/icons' 


export default {
  name: 'DashboardSimples',
  components: {
    MainChartExample,
    WidgetsDropdown,
    WidgetsBrand,
  },
  pencil: {
    cilBell
    
  },
  data () {
    return {
      alert: {
        id: 0,
        name: '',
        alert_text: ''
      },
      alert2: true,
      show_alert: true,
      
    }
  },
  created () {
    axios.get('http://localhost:8000/api/one/alert/2').then(response => {

      console.log(response.data.alert)
      this.alert = response.data.alert;
    })
    .catch(error => {
      this.errorMessage = error.message;
      console.error("There was an error!", error);
    });
  }

}
</script>

<style>

  .main-card {
    position: relative;
    width: 300px;
  }

  .button-drop {
    position: relative;
    left: 250px;
    bottom: 20px;
  }

  .estat {
    position: relative;
    top: 30px;
    left: 20px;
  }

  .header-img {
    position: relative;
    right: 150px;
    top: 20px;
  }

  .alert-txt {
    position: relative;
    right: 20px;
  }

  .alert-icon {
    position: relative;
    left: 60px;
  }


</style>