import { ComponentFixture, TestBed } from '@angular/core/testing';

import { VennEffComponent } from './venn-eff.component';

describe('VennEffComponent', () => {
  let component: VennEffComponent;
  let fixture: ComponentFixture<VennEffComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ VennEffComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(VennEffComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
