describe("Add/Remove Elements Tests", () => {
  beforeEach(() => {
    cy.visit("/add_remove_elements/"); // works with baseUrl
  });

  it("Add 3 elements", () => {
    for (let i = 0; i < 3; i++) {
      cy.contains("Add Element").click();
    }
    cy.get(".added-manually").should("have.length", 3);
  });

  it("Remove one element", () => {
    for (let i = 0; i < 3; i++) {
      cy.contains("Add Element").click();
    }
    cy.get(".added-manually").first().click();
    cy.get(".added-manually").should("have.length", 2);
  });

  it("Remove all elements", () => {
    for (let i = 0; i < 3; i++) {
      cy.contains("Add Element").click();
    }
    cy.get(".added-manually").each(($el) => {
      cy.wrap($el).click();
    });
    cy.get(".added-manually").should("have.length", 0);
  });
});
