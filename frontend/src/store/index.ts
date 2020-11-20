import Vue from "vue";
import Vuex from "vuex";

Vue.use(Vuex);

interface Store {
  articles: any[],
  ways: object,
  waysIds: object,
  articlesIds: object,
  waysMode: boolean,
  selectedArticle: string,
  showHideContextMenu: object | null,
  selectedWay: [any]
}


export default new Vuex.Store({
  state: {
    articles: [],
    ways: {},
    waysIds: {},
    articlesIds: {},
    waysMode : true,
    selectedArticle: '',
    showHideContextMenu: { id: null, x: 0, y: 0 },
    selectedWay: [0]
  },
  mutations: {
    setWays( state: Store, arg ) { state.ways = arg },
    setWaysIDs( state: Store, arg ) { state.waysIds = arg },
    setArticlesIDs( state: Store, arg ) { state.articlesIds = arg },
    setWaysMode( state: Store, arg ) { state.waysMode = arg },
    setSelectedArticle( state: Store, arg ) { state.selectedArticle = arg },    
    setContextShow(state: Store, arg) { state.showHideContextMenu = arg},
    setSelectedWay(state: Store, arg) { state.selectedWay = arg }
  },
  actions: {

  },
  modules: {},
});
