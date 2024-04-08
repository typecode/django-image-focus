(function () {
    class PointWidget {
        constructor(elem) {
            this.displayValue = {
                x: 0.5,
                y: 0.5
            }
            
            this.getDOM(elem)
            this.getLoadedValue()
            this.addEventListeners()
            this.updateDisplay()
        }
        
        getDOM (elem) {
            this.displayFieldX = elem.querySelector('.imagefocus-point-widget__display-x')
            this.displayFieldY = elem.querySelector('.imagefocus-point-widget__display-y')
            this.hiddenField = elem.querySelector('input[type="hidden"]')
        }

        getLoadedValue () {
            const value = this.hiddenField.value.split(',')
            this.displayValue = { x: value[0], y: value[1] }
        }

        addEventListeners () {
            this.hiddenField.addEventListener("change", (evnt) => this.handleHiddenFieldChange(evnt))
            this.displayFieldX.addEventListener("change", (evnt) => this.handleDisplayFieldChange(evnt, "x"))
            this.displayFieldY.addEventListener("change", (evnt) => this.handleDisplayFieldChange(evnt, "y"))
        }

        handleHiddenFieldChange (evnt) {
            const value = this.hiddenField.value.split(',')
            this.updateValue(value[0], value[1])
        }

        handleDisplayFieldChange (evnt, axis) {
            const value = parseFloat(evnt.target.value)
            if (isNaN(value)) {
                evnt.target.value = this.displayValue[axis]
                return
            }
            if (value < 0) {
                evnt.target.value = 0
            } else if (value > 1) {
                evnt.target.value = 1
            }

            if (axis === "x") {
                this.updateValue(evnt.target.value, this.displayValue.y)
            }
            if (axis === "y") {
                this.updateValue(this.displayValue.x, evnt.target.value)
            }
            this.hiddenField.dispatchEvent(new Event('update'))
        }

        updateValue (x, y) {
            this.displayValue = { x, y }
            this.hiddenField.value = `${x},${y}`
            this.updateDisplay()
        }

        updateDisplay () {
            this.displayFieldX.value = this.displayValue.x
            this.displayFieldY.value = this.displayValue.y
        }

    }

    const imagefocuspoint = (function () {
        let pointWidgets = []

        const init = () => {
            const pointWidgetContainers = document.querySelectorAll('.imagefocus-point-widget');
            pointWidgetContainers.forEach((fileinput) => {
                const pointWidget = new PointWidget(fileinput)
                pointWidgets.push(pointWidget)
            })
        }
        return {
            init
        }
    })();

    const djangoPollingInterval = setInterval(() => {
        if (window.django && window.django.jQuery) {
            clearInterval(djangoPollingInterval)
            window.django.jQuery(() => imagefocuspoint.init())
        }
    }, 100)
})()