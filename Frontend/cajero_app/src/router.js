import vueRouter from 'vue-router'
import Inicio from './components/Inicio'
import UserBalance from './components/UserBalance'
import Formulario from './components/Formulario'
import Reserva from './components/Reserva'

import App from './App'

const router = new vueRouter({
        mode: 'history',
        base: __dirname,
        routes: [
            {
                path: '/',
                name: "root",
                component: App
            },
            {
                path: '/Reservas.com/',
                name: "user",
                component: Inicio
            },
            {
                path: '/user/balance/:username',
                name: "user_balance",
                component: UserBalance
            },
            {
                path: '/Ingreso/',
                name: "Formulario",
                component: Formulario
            },
            {
                path: '/Reservar/',
                name: "Reserva",
                component: Reserva
            },
        ]
    })

export default router