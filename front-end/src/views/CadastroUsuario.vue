<template>
  <div class="c-app flex-row align-items-center">
    <CContainer>
      <CRow class="justify-content-center">
        <CCol md="6">
          <CCardGroup>
            <CCard class="p-4">
              <CCardBody>
                <CForm>
                  <h1 class = "text-center"> Cadastro de Usuários</h1>

                  <p class="text-muted">Registre aqui os usuários que terão acesso restrito às configurações e estatísticas avançadas</p>
                  <CInput
                    placeholder="Escolha um nome de usuário"
                    autocomplete="username email"
                  >
                    <template #prepend-content><CIcon name="cil-user"/></template>
                  </CInput>
                  <CInput
                    placeholder="Digite uma senha"
                    type="password"
                    autocomplete="curent-password"
                  >
                    <template #prepend-content><CIcon name="cil-lock-locked"/></template>
                  </CInput>
                  <CRow>



                    <div class="row button"> 
                       <CCardBody>
                        <CHeaderNavLink to="/painelAdmin">
                          <CButton size="lg" color="secondary" block>Voltar ao Painel</CButton>
                        </CHeaderNavLink>
                       </CCardBody>
                       
                    </div>   

                    <div class="row dashboard-button">  

                      <CCardBody>
                        <CButton size="lg" color="secondary" block>Cadastrar</CButton>
                       </CCardBody>


                    </div> 

                  </CRow>
                </CForm>
              </CCardBody>
            </CCard>

          </CCardGroup>
        </CCol>
      </CRow>
    </CContainer>
  </div>
</template>

<script>
export default {
  name: 'Login'
}
</script>

<style>
.button {
  position: relative;
  left: 2%;
}

.dashboard-button {
  position: relative;
  left: 38%;
}

</style>
