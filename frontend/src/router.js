import contact from './components/contact'
import aboutme from './components/aboutme'
import past_projects from './components/past_projects'

export default [
  {path: '/', component: aboutme},
  {path: '/contact', component: contact},
  {path: '/past', component: past_projects}
]
