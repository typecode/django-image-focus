(function () {
    class FileWidget {
        constructor(elem) {
            this.getDOM(elem)
            this.addEventListeners()
            this.getFocusPointInputValue()
            this.updateFocalPoint()
        }
        
        getDOM (elem) {
            this.rootEl = elem
            this.fileInput = elem.querySelector('input[type="file"]')
            this.focusInput = document.querySelector('.imagefocus-input[data-image-field="' + this.fileInput.name + '"]')
            this.imageFrame = elem.querySelector('.imagefocus-file-upload__image')
            this.previewImage = this.imageFrame.querySelector('img')
            this.inputName = this.fileInput.name
            this.focusPointIndicator = elem.querySelector('.imagefocus-file-upload__focus-point')
        }

        getFocusPointInputValue () {
            const focusPointValue = this.focusInput.value.split(',')
            this.setFocalPoint(focusPointValue[0], focusPointValue[1])
        }

        addEventListeners () {
            this.imageFrame.addEventListener('click', (evnt) => this.handleFocusPointClick(evnt))
            this.fileInput.addEventListener('change', (evnt) => this.handleFileChange(evnt))
            this.focusInput.addEventListener('update', (evnt) => this.getFocusPointInputValue())
        }

        handleFocusPointClick (evnt) {
            const x = (evnt.offsetX / this.imageFrame.clientWidth).toFixed(2)
            const y = (evnt.offsetY / this.imageFrame.clientHeight).toFixed(2)
            this.setFocalPoint(x, y)
        }

        setFocalPoint (x, y) {
            this.focusPointValue = { x, y }
            this.focusInput.value = `${x},${y}`
            this.focusInput.dispatchEvent(new Event('change'))
            this.updateFocalPoint()
        }

        updateFocalPoint () {
            this.focusPointIndicator.style.left = `${this.focusPointValue.x * 100}%`
            this.focusPointIndicator.style.top = `${this.focusPointValue.y * 100}%`
        }

        handleFileChange (evnt) {
            const file = this.fileInput.files[0]
            if (!file) return
            const reader = new FileReader()
            reader.onload = (evnt) => {
                this.previewImage.src = evnt.target.result
                this.setFocalPoint(0.5, 0.5)
            }
            reader.readAsDataURL(file)
        }
    }

    const imagefocus = (function () {
        let fileWidgets = []

        const init = () => {
            const fileinputs = document.querySelectorAll('.imagefocus-file-upload');
            fileinputs.forEach((fileinput) => {
                const fileWidget = new FileWidget(fileinput)
                fileWidgets.push(fileWidget)
            })
        }
        return {
            init
        }
    })();

    const djangoPollingInterval = setInterval(() => {
        if (window.django && window.django.jQuery) {
            clearInterval(djangoPollingInterval)
            window.django.jQuery(() => imagefocus.init())
        }
    }, 100)
})()