/**
User details
 */

'use strict'

const m = require('mithril')

const Dashboard = {
  view(vnode) {
    return [
      m('.header.text-center.mb-4',
        m('h4', 'Welcome To'),
        m('h1.mb-3', 'Agro Smart'),
        m('h5',
          m('em',
            ' ',
            m('strong', '')))),
      m('.blurb',
        m('p',
          m('em', ''),
          ' ',
          ' ',
          ' ',
          ' ',
          ''),
        m('',
          m('em', ''),
          ' ',
          ' ',
          '',
          ' '),
        m('p',
          '',
          m('em', ''),
          ', ',
          ' ',
          ' ',
          ''))
    ]
  }
}

module.exports = Dashboard
