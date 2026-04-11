import './style.css'

document.addEventListener('DOMContentLoaded', () => {

  // 1. Intersection Observer for Scroll Reveals
  const revealElements = document.querySelectorAll('.observer-reveal');
  
  const revealOptions = {
    threshold: 0.15,
    rootMargin: "0px 0px -50px 0px"
  };

  const revealOnScroll = new IntersectionObserver(function(entries, observer) {
    entries.forEach(entry => {
      if (!entry.isIntersecting) {
        return;
      } else {
        entry.target.classList.add('visible');
        observer.unobserve(entry.target);
      }
    });
  }, revealOptions);

  revealElements.forEach(el => {
    revealOnScroll.observe(el);
  });

  // 2. Glitch Text Effect Hover
  const glitchText = document.querySelector('.glitch');
  if (glitchText) {
    // Only applied on desktop to preserve battery on mobile
    glitchText.addEventListener('mouseenter', () => {
      glitchText.style.animation = "glitch-anim 0.3s cubic-bezier(0.25, 0.46, 0.45, 0.94) both infinite";
    });
    glitchText.addEventListener('mouseleave', () => {
      glitchText.style.animation = "none";
    });
  }

  // 3. Dynamic Typewriter for the Contact CLI Input
  const cliInput = document.getElementById('cli-input');
  if (cliInput) {
    const defaultPlaceholder = cliInput.getAttribute('placeholder');
    let i = 0;
    cliInput.setAttribute('placeholder', '');
    
    // We wait 2 seconds after the observer makes the contact section visible,
    // but a simpler way is just to type it out when it intersects
    const cliObserver = new IntersectionObserver((entries) => {
      entries.forEach(entry => {
        if(entry.isIntersecting) {
          typeWriter();
          cliObserver.unobserve(entry.target);
        }
      });
    }, { threshold: 0.5 });
    
    cliObserver.observe(document.querySelector('.cli-input-wrapper'));

    function typeWriter() {
      if (i < defaultPlaceholder.length) {
        cliInput.setAttribute('placeholder', defaultPlaceholder.substring(0, i + 1));
        i++;
        setTimeout(typeWriter, 50);
      }
    }

    cliInput.addEventListener('keydown', (e) => {
      if (e.key === 'Enter') {
        const val = cliInput.value.trim();
        if (val) {
          window.location.href = `mailto:VrtxOmega@pm.me?subject=Portfolio Outreach&body=${encodeURIComponent(val)}`;
          cliInput.value = '';
          cliInput.setAttribute('placeholder', 'Message sent to mail client...');
        }
      }
    });
  }

  // 4. Parallax effect for the 3D rotating hologram ring
  const ringContainer = document.querySelector('.rotating-hologram');
  if (ringContainer) {
    document.addEventListener('mousemove', (e) => {
      const centerX = window.innerWidth / 2;
      const centerY = window.innerHeight / 2;
      
      const moveX = (e.clientX - centerX) / 30;
      const moveY = (e.clientY - centerY) / 30;
      
      // Gentle parallax shift on the rings based on mouse
      ringContainer.style.transform = `translateX(${moveX}px) translateY(${moveY}px)`;
    });
  }

});
