import { ComponentFixture, TestBed } from '@angular/core/testing';

import { HistogramPositionsComponent } from './histogram-positions.component';

describe('HistogramPositionsComponent', () => {
  let component: HistogramPositionsComponent;
  let fixture: ComponentFixture<HistogramPositionsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ HistogramPositionsComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(HistogramPositionsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
