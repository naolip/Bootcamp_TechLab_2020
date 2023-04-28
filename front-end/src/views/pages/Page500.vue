<template>

  
  <CContainer class="d-flex align-items-center min-vh-100">
    <CRow class="w-100 justify-content-center">
      <CCol md="6">

         <CHeader fixed with-subheader light>
    <CToggler
      in-header
      class="ml-3 d-lg-none"
      @click="$store.commit('toggleSidebarMobile')"
    />
    <CToggler
      in-header
      class="ml-3 d-md-down-none"
      @click="$store.commit('toggleSidebarDesktop')"
    />
    <CHeaderBrand class="mx-auto d-lg-none" to="/">
      <CIcon name="logo" height="48" alt="Logo"/>
    </CHeaderBrand>
    <CHeaderNav class="d-md-down-none mr-auto">
      <CHeaderNavItem class="px-3">
        <CHeaderNavLink to="/dashboard">
          Dashboard
        </CHeaderNavLink>
      </CHeaderNavItem>
      <CHeaderNavItem class="px-3">
        <CHeaderNavLink to="/users" exact>
          Users
        </CHeaderNavLink>
      </CHeaderNavItem>
      <CHeaderNavItem class="px-3">
        <CHeaderNavLink>
          Settings
        </CHeaderNavLink>
      </CHeaderNavItem>
    </CHeaderNav>
    <CHeaderNav class="mr-4">
      <CHeaderNavItem class="d-md-down-none mx-2">
        <CHeaderNavLink>
          <CIcon name="cil-bell"/>
        </CHeaderNavLink>
      </CHeaderNavItem>
      <CHeaderNavItem class="d-md-down-none mx-2">
        <CHeaderNavLink>
          <CIcon name="cil-list"/>
        </CHeaderNavLink>
      </CHeaderNavItem>
      <CHeaderNavItem class="d-md-down-none mx-2">
        <CHeaderNavLink>
          <CIcon name="cil-envelope-open"/>
        </CHeaderNavLink>
      </CHeaderNavItem>
      <TheHeaderDropdownAccnt/>
    </CHeaderNav>
    <CSubheader class="px-3">
      <CBreadcrumbRouter class="border-0 mb-0"/>
    </CSubheader>
  </CHeader>

<CRow>

      <CCol sm="6" lg="6">
        <CWidgetProgress
          header="Uso de Máscara"
          text="Porcentagem de pessoas com máscara nas dependências"
          footer="91% Pessoas com mascara"
          class="card-header-action position-relative"
          style="right:5px; top:5px"
          color="success"
          :value="91"
        />
      </CCol>

      <CCol sm="6" lg="6">
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


      <CCol col="12" sm="6" lg="6">
        <CWidgetIcon
          header="Salas Livres"
          text="10"
          color="info"
        >
          <CIcon name="cil-laptop" width="24"/>
        </CWidgetIcon>
      </CCol>
      <CCol col="12" sm="1" lg="6">
        <CWidgetIcon
          header="Salas Ocupadas"
          text="3"
          color="danger"
        >
          <CIcon name="cil-bell" width="24"/>
        </CWidgetIcon>
      </CCol>
</CRow>       


        <CCardBody>
          <CAlert show color="warning">
            <h4 class="alert-heading">CUIDADO!!!</h4>
            <p>
              O numero de pessoas sem mascara esta proximo ao maximo permitido
            </p>
            <hr>
            <p class="mb-0">
              Vista sua mascara e va para um local seguro
            </p>
          </CAlert>
        </CCardBody>

        </CCol>
          <CCol sm xs="12" class="text-center mt-3">
            <CButton color="danger" shape="pill">
              <CIcon name="cil-lightbulb"/>&nbsp;Bug Report
           </CButton>
        </CCol>

 



<!--
        <div class="clearfix">
          <h1 class="float-left display-3 mr-4">500</h1>
          <h4 class="pt-3">Houston, we have a problem!</h4>
          <p class="text-muted">The page you are looking for is temporarily unavailable.</p>
        </div>
        <CInput
          class="mb-3"
          placeholder="What are you looking for?"
        >
          <template #prepend-content><CIcon name="cil-magnifying-glass"/></template>
          <template #append>
            <CButton color="info">Search</CButton>
          </template>
        </CInput>

-->

      <CButton  size="lg" color="danger" block>Block level button</CButton>

     
    </CRow>
  </CContainer>
</template>

<script>
export default {
  name: 'Page500'
}
</script>
