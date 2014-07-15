function SelectorMap() {}

SelectorMap.prototype.init = function () {
    var propertyToSelectorMap = {
        body: 'body, footer',
        menu: '.menu',
        menuTrigger: '.menu-trigger',
        scheduleTrigger: '[href="#schedule"], .sequence-list .close',
        creditTrigger: '[href="#credit"]'
    };

    for (k in propertyToSelectorMap) {
        this[k] = $(propertyToSelectorMap[k]);
    }
};

function Menu(selector) {
    this.selector = selector;
}

Menu.prototype.init = function () {
    this.selector.menu.css('top', this.selector.menuTrigger.outerHeight());
};

Menu.prototype.deactivateAll = function (e) {
    this.selector.body.removeClass('credit-active');
    this.selector.body.removeClass('schedule-active');
    this.selector.body.removeClass('menu-active');
};

Menu.prototype.triggerOnActivation = function (e) {
    e.preventDefault();
    e.stopPropagation();

    this.init();

    this.selector.body.toggleClass('menu-active');
};

Menu.prototype.triggerSchedule = function (e) {
    e.preventDefault();
    e.stopPropagation();

    this.selector.body.toggleClass('schedule-active');
    this.selector.body.removeClass('menu-active');
};

Menu.prototype.triggerCredit = function (e) {
    e.preventDefault();
    e.stopPropagation();

    this.selector.body.toggleClass('credit-active');
    this.selector.body.removeClass('menu-active');
};

var s = new SelectorMap(), // selector_map
    m = new Menu(s)
;

function main() {
    s.init();
    m.init();

    s.body.addClass('ready');

    s.body.on('click', $.proxy(m.deactivateAll, m));
    s.menuTrigger.on('click', $.proxy(m.triggerOnActivation, m));
    s.creditTrigger.on('click', $.proxy(m.triggerCredit, m));
    s.scheduleTrigger.on('click', $.proxy(m.triggerSchedule, m));
}

$(document).ready(main);