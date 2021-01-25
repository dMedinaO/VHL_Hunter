import { ComponentFixture, TestBed } from '@angular/core/testing';

import { HeatmapPositionsComponent } from './heatmap-positions.component';

describe('HeatmapPositionsComponent', () => {
  let component: HeatmapPositionsComponent;
  let fixture: ComponentFixture<HeatmapPositionsComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ HeatmapPositionsComponent ]
    })
    .compileComponents();
  });

  beforeEach(() => {
    fixture = TestBed.createComponent(HeatmapPositionsComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
