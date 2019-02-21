import Vue from 'vue'
import Vuex from 'vuex'
import { Event } from '../api/events'
import {
  ADD_EVENT,
} from './mutation-types.js'

Vue.use(Vuex)

// Состояние
const state = {
  events: []  // список заметок
}

// Геттеры
const getters = {
  events: state => state.events  // получаем список заметок из состояния
}

// Мутации
const mutations = {
  // Добавляем заметку в список
  [ADD_EVENT] (state, {events}) {
    state.events = events
  }
}

// Действия
const actions = {
  addEvent ({ commit }) {
    Event.add().then(response => {
      return response.text
    })
  }
}

export default new Vuex.Store({
  state,
  getters,
  actions,
  mutations
})
