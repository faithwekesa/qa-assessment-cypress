describe('User Registration Form Automation', () => {

  it('should successfully fill out and submit the registration form', () => {
    Cypress.on('uncaught:exception', () => {
      return false;
    });

    cy.visit('https://saucedemo.com');

    cy.get('#user-name').type('Faith').should('have.value', 'Faith');
    cy.get('#password').type('Password123').should('have.value', 'Password123');
    cy.get('#login-button').should('be.visible').click();
  });
  
});


