import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SwalLegendComponent } from './swal-legend.component';

describe('SwalLegendComponent', () => {
  let component: SwalLegendComponent;
  let fixture: ComponentFixture<SwalLegendComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ SwalLegendComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(SwalLegendComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
