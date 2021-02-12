import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SankeyEffComponent } from './sankey-eff.component';

describe('SankeyEffComponent', () => {
  let component: SankeyEffComponent;
  let fixture: ComponentFixture<SankeyEffComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SankeyEffComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SankeyEffComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
