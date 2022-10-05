import { createRouter, createWebHashHistory } from 'vue-router'
import App from './App.vue'
import usuario from './components/usuario.vue'
import psalud from './components/psalud.vue'
import paciente from './components/paciente.vue'
import familiar from './components/familiar.vue'
import viewusuario from './components/viewusuario.vue'
import LogIn from './components/LogIn.vue'

const routes = [
  {
    path: '/',
    name: 'root',
    component: App
  },
  {
    path: '/user/login',
    name: 'LogIn',
    component: LogIn
  },
  {
    path: '/registro/usuario',
    name: 'regUsuario',
    component: usuario
  },
  {
    path: '/registro/psalud',
    name: 'regPsalud',
    component: psalud
  },
  {
    path: '/registro/paciente',
    name: 'regPaciente',
    component: paciente
  },
  {
    path: '/registro/familiar',
    name: 'regFamiliar',
    component: familiar
  },
  {
    path: '/consulta/paciente',
    name: 'viewpaciente',
    component: viewusuario
  }
     
]

const router = createRouter({
  history: createWebHashHistory(),
  routes
})

export default router
